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

# State Machine for the Cobot
import sys
sys.path.append('../chef_bot_RCS/')
from cobot_state import CobotControl

# Adjust Window Size for the PI
from kivy.core.window import Window
Window.size = (800, 500)

# Text Updater
from kivy.properties import StringProperty

__author__ = 'Alex Tejada'

kivyFile = 'main.kv'

class MainWindow(GridLayout):
    pass

class MenuPopup(FloatLayout):
    pass

class MainApp(App):

    # Main Menu Color Decorators
    chef_bot_black = '2F3638'
    chef_bot_light = 'FEFFFE'
    chef_bot_gray = 'D6D6D6'
    chef_bot_primary = 'B3E0DB'
    chef_bot_secondary = 'DAE8D3'
    chef_bot_tertiary = 'F7F3E3'

    # Declarations
    cobotController = CobotControl()
    Status = StringProperty(str(cobotController.state))
    RC = 'Request Confirmed'
    

    def MainApp (self):
        self.request = 'empty'
        self.popupWindow = object()

    def build(self):
        return MainWindow()
    
    def Pressbtn(self, instance):
        self.request = instance.text
        print('[INFO   ] [Cobot App   ] Requesting ', self.request)
        show = MenuPopup()
        self.popupWindow = Popup(title="Requested " + self.request + '?', title_align='center', 
                content=show, size_hint=(None, None), size=(400,250))
        self.popupWindow.open()
    
    def ConfirmSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.request + ' Confirmed. ')
        self.popupWindow.dismiss()
        self.cobotController.on_event(self.RC)
        self.Status = str(self.cobotController.state)

    def DeclineSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + self.request + ' Cancelled. ')
        self.popupWindow.dismiss()

    def AppExit(self, isinstance):
        pass

        # send request to Armando's part
        # get a reponse from the model 
        # send to Heidi's part 

# End of app delcaration

if __name__ == "__main__":
    app = MainApp()
    app.run() 