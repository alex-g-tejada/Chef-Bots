# Main Kivy application class
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, BooleanProperty

# State Machine for the Cobot
import sys
sys.path.append('../chef_bot_RCS/')
from cobot_state import CobotControl
#from chef_bot_RCS.cobot_state import CobotControl
# Adjust Window Size for the PI
from kivy.core.window import Window
from kivy.config import Config
Builder.load_file('mainapp.kv')
Window.size = (800, 500)

__author__ = 'Alex Tejada'

class CancelBtn(Button):

    #enabled = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(CancelBtn, self).__init__(*args, **kwargs)
        self.popupWindow = object()
        CancelBtn.disabled = False

    def on_enabled(self, value):
        if value:
            self.background_color = [1,1,1,1]
            self.color = [1,1,1,1]
            CancelBtn.disabled = value
        else:
            self.background_color = [1,1,1,.3]
            self.color = [1,1,1,.5]

    def on_touch_down(self, touch):

        if True == CancelBtn.disabled:
            #print('[INFO   ] [Cobot App   ] Cancel Button Push ', CancelBtn.disabled)
            self.on_press()
            return super(self.__class__, self).on_touch_down(touch)

"""
Screen to display individual set of ingredients
"""
class OneSelectScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

"""
Screen to allow the user to individually select the ingrients
the cobot should find
"""
class MultSelectScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

"""
Landing page for the application that will greet the user
"""
class GreeterScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

"""
Popup Window for user confirmation of a topping
"""
class MenuPopup(FloatLayout):
    pass

class MenuPopup_Mult(FloatLayout):
    pass

class MenuPopup_Can(FloatLayout):
    pass

class MenuPopup_Error(FloatLayout):
    pass

class MenuPopup_Exit(FloatLayout):
    pass

class MainApp(App):

    # Main Menu Color Decorators
    chef_bot_black = '2F3638'
    chef_bot_light = 'FEFFFE'
    chef_bot_gray = 'D6D6D6'
    chef_bot_primary = 'B3E0DB'
    chef_bot_secondary = 'DAE8D3'
    chef_bot_tertiary = 'F7F3E3'

    # Cobot State controller
    cobotController = CobotControl()
    # String holding the state of the controller
    Status = StringProperty(str(cobotController.state))

    # State Keys
    RC = 'Request Confirmed'
    SC = 'Setup Complete'
    ER = 'Error'
    NF = 'Not Found'
    FR = 'Found Request'
    PC = 'Point Complete'
    FC = 'Request Completed'

    # Burger Ingredients
    tomatoes = 'Tomatoes'
    lettuce = 'Lettuce'
    pickles = 'Pickles'
    cheese = 'Cheese'
    onions = 'Onions'

    # Messages
    message_processing = "Order still processing"
    message_complete = "Order completed!"
    message_exit = "Would you like to exit the application?"

    # List of Ingredients selected
    toppingList = []

    request = 'empty'

    def MainApp (self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screenmanager = ScreenManager()
        self.Cbtn = CancelBtn()
        self.screenmanager.add_widget(GreeterScreen(name="screen_one"))
        self.screenmanager.add_widget(OneSelectScreen(name="screen_two"))
        self.screenmanager.add_widget(MultSelectScreen(name="screen_three"))
        self.popupWindow = object()

    def build(self):
        self.title = 'Chef Bots'
        self.__init__()
        return self.screenmanager

    def toppinglist_toString(self):
        s = str(self.toppingList)
        s = s.replace("'","")
        s = s.replace("[","")
        s = s.replace("]","")
        return s

    def startOperation(self):
        # Entering Detection State
        self.cobotController.on_event(self.RC)
        self.cobotController.run_state(self.toppingList)
        # Entering Response State
        self.cobotController.on_event(self.SC)
        results = self.cobotController.run_state(self.toppingList)
        print("[INFO   ] [Cobot App   ] AI Results: ", results)
        # Entering PinPoint State
        self.cobotController.on_event(self.FR)
        results = self.cobotController.run_state(self.toppingList)
        print("[INFO   ] [Cobot App   ] Pinpoint Results: ", results)
        # Completed Order
        self.requestMessage(self.message_complete)

    def getOrder(self, order):
        self.toppingList = []
        if order == 'Deluxe':
            self.toppingList.extend([self.tomatoes, self.lettuce, self.pickles, self.cheese, self.onions])
        elif order == 'Plain':
            self.toppingList.extend([self.pickles, self.cheese])
        else:
            self.toppingList.append(self.tomatoes)

    def requestMessage(self, message):
        show = MenuPopup_Error()
        self.popupWindow = Popup(title=message, title_align='center', separator_color= [254/255.,255/255,254/255.,1.],
                content=show, size_hint=(None, None), size=(280,200), background = 'images/Popup2.png')
        self.popupWindow.open()

    def Pressbtn(self, instance):
        if self.cobotController.RS != str(self.cobotController.state):
            print("[INFO   ] [Cobot App   ] Not in the receive state.")
            self.requestMessage(self.message_processing)
        else:
            self.request = instance.text
            print('[INFO   ] [Cobot App   ] Requesting ', self.request)
            self.getOrder(self.request)
            show = MenuPopup()
            self.popupWindow = Popup(title="Requested " + self.request + ': ' + self.toppinglist_toString(), title_align='center', separator_color= [254/255.,255/255,254/255.,1.],
                    content=show, size_hint=(None, None), size=(350,250), background = 'images/Popup2.png')
            self.popupWindow.open()

    def itemSelect(self, text, state):
        is_box_on = state
        print('[INFO   ] [Cobot App   ] Checkbox State: ', is_box_on)
        print('[INFO   ] [Cobot App   ] Checkbox Selected: ', self.toppingList)

        if is_box_on == 'down':
            item = text
            self.toppingList.append(item)
            print('[INFO   ] [Cobot App   ] Checkbox Selected: ', self.toppingList)
        elif is_box_on == 'normal':
            item = text
            self.toppingList.remove(item)
            print('[INFO   ] [Cobot App   ] Checkbox Selected: ', self.toppingList)

    def Submitbtn(self, instance):
        if self.cobotController.RS != str(self.cobotController.state):
            print("[INFO   ] [Cobot App   ] Not in the receive state.")
            self.requestMessage(self.message_processing)

        elif len(self.toppingList) > 0:
            print('[INFO   ] [Cobot App   ] Requesting ', self.toppingList)
            requesting = self.toppinglist_toString()
            show = MenuPopup_Mult()
            self.popupWindow = Popup(title="Requesting: " + requesting + '?', title_align='center', separator_color= [254/255.,255/255,254/255.,1.],
                    content=show, size_hint=(None, None), size=(350,250), background = 'images/Popup2.png')
            self.popupWindow.open()
        else:
            show = MenuPopup_Error()
            self.popupWindow = Popup(title="No selection was made", title_align='center', separator_color= [254/255.,255/255,254/255.,1.],
                    content=show, size_hint=(None, None), size=(280,200), background = 'images/Popup2.png')
            self.popupWindow.open()

    def ConfirmMultSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.toppinglist_toString() + ' Confirmed. ')
        self.popupWindow.dismiss()
        self.Cbtn.on_enabled(True)
        self.startOperation()
        #self.Status = str(self.cobotController.state)
        #self.cobotController.run_state("RC")

    def ConfirmSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.request + ' Confirmed. ')
        self.popupWindow.dismiss()
        self.startOperation()
        #self.Status = str(self.cobotController.state)
        #self.cobotController.run_state('start')

    def DeclineSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.request + ' Cancelled. ')
        self.popupWindow.dismiss()

    def DeclineSel_Mult(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.toppinglist_toString() + ' Cancelled. ')
        self.popupWindow.dismiss()

    def Dismiss(self, instance):
        self.popupWindow.dismiss()

    def Cancel(self, instance):
        if self.cobotController.RS != str(self.cobotController.state):
            show = MenuPopup_Can()
            self.popupWindow = Popup(title="Cancel order?", title_align='center', separator_color= [254/255.,255/255,254/255.,1.],
                    content=show, size_hint=(None, None), size=(300,200), background = 'images/Popup2.png')
            self.popupWindow.open()
        else:
            show = MenuPopup_Error()
            self.popupWindow = Popup(title="No requests are running", title_align='center', separator_color= [254/255.,255/255,254/255.,1.],
                    content=show, size_hint=(None, None), size=(280,200), background = 'images/Popup2.png')
            self.popupWindow.open()

    def stopOrder(self, instance):
        print('[INFO   ] [Cobot RCS   ] Returning to ReceiveState...')
        self.popupWindow.dismiss()
        self.cobotController.on_event(self.ER)
        self.cobotController.state_reset()
        #self.toppingList = []
        print('[INFO   ] [Cobot RCS   ] Done')

    def AppExit(self):
        show = MenuPopup_Exit()
        self.popupWindow = Popup(title=self.message_exit, title_align='center', separator_color= [254/255.,255/255,254/255.,1.],
                content=show, size_hint=(None, None), size=(300,200), background = 'images/Popup2.png')
        self.popupWindow.open()
        print("[INFO   ] [Cobot App   ] Exiting applicaiton....")


# End of app delcaration

if __name__ == "__main__":
    Config.set('graphics', 'fullscrenn','auto')
    Config.set('graphics','window_state','maximized')
    Config.write()
    app = MainApp()
    app.run()
