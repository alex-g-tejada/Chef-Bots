# Main Kivy application class
from kivy.app import App
import kivy
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget 
from kivy.uix.actionbar import ActionBar, ActionButton
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.properties import StringProperty

# State Machine for the Cobot
import sys
sys.path.append('../chef_bot_RCS/')
from cobot_state import CobotControl

# Adjust Window Size for the PI
from kivy.core.window import Window
from kivy.config import Config
Window.size = (800, 500)


__author__ = 'Alex Tejada'


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


class TestS(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(TestS, self).__init__(*args, **kwargs)
        self.orientation="horizontal"


class TestScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(TestScreen, self).__init__(*args, **kwargs)
        self.count_box = 1
        self.add_widget(Button())


"""
Popup Window for user confirmation of a topping
"""
class MenuPopup(FloatLayout):
    pass

class MenuPopup_Mult(FloatLayout):
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
    # States
    RS = "ReceiveState"
    DS = "DetectionState"
    SS = "ResponseState"
    PS = "PinPointState"
    CS = "CancelOrderState"
    
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

    # List of Ingredients selected
    toppingList = []

    request = 'empty'

    # Screen Manager 
    #screenmanager = ScreenManager()

    def MainApp (self):
        self.popupWindow = object()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screenmanager = ScreenManager()
        self.screenmanager.add_widget(TestScreen(name="test"))
        #self.screenmanager.add_widget(GreeterScreen(name="screen_one"))
        #self.screenmanager.add_widget(OneSelectScreen(name="screen_two"))
        #self.screenmanager.add_widget(MultSelectScreen(name="screen_three"))
        

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

    def Pressbtn(self, instance):
        self.request = instance.text
        print('[INFO   ] [Cobot App   ] Requesting ', self.request)
        show = MenuPopup()
        self.popupWindow = Popup(title="Requested " + self.request + '?', title_align='center', 
                content=show, size_hint=(None, None), size=(400,250))
        self.popupWindow.open()
    
    def itemSelect(self, text, state):
        is_box_on = state
        print('[INFO   ] [Cobot App   ] Checkbox State: ', is_box_on)
        
        if is_box_on == 'down':
            item = text
            print('[INFO   ] [Cobot App   ] Checkbox Selected: ', text)
            self.toppingList.append(item)
            print('[INFO   ] [Cobot App   ] Checkbox Selected: ', self.toppingList)
        elif is_box_on == 'normal':
            item = text
            print('[INFO   ] [Cobot App   ] Checkbox Selected: ', text)
            self.toppingList.remove(item)
            print('[INFO   ] [Cobot App   ] Checkbox Selected: ', self.toppingList)
        
    def Submitbtn(self, instance):
        if len(self.toppingList) > 0:
            print('[INFO   ] [Cobot App   ] Requesting ', self.toppingList)
            requesting = self.toppinglist_toString()
            show = MenuPopup_Mult()
            self.popupWindow = Popup(title="Requesting: " + requesting + '?', title_align='center', 
                    content=show, size_hint=(None, None), size=(400,250))
            self.popupWindow.open()
            

    def ConfirmMultSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.toppinglist_toString() + ' Confirmed. ')
        self.popupWindow.dismiss()
        self.cobotController.on_event(self.RC)
        self.Status = str(self.cobotController.state)

    def ConfirmSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.request + ' Confirmed. ')
        self.popupWindow.dismiss()
        self.cobotController.on_event(self.RC)
        self.Status = str(self.cobotController.state)

    def DeclineSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.request + ' Cancelled. ')
        self.popupWindow.dismiss()

    def DeclineSel_Mult(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.toppinglist_toString() + ' Cancelled. ')
        self.popupWindow.dismiss()

    def AppExit(self, isinstance):
        pass

        # send request to Armando's part
        # get a reponse from the model 
        # send to Heidi's part 

# End of app delcaration

if __name__ == "__main__":  
    Config.set('graphics', 'fullscrenn','auto')
    Config.set('graphics','window_state','maximized')
    Config.write()
    app = MainApp()
    app.run() 