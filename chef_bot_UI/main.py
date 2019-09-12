# Main Kivy application class
from kivy.app import App
# User Interface Components
import kivy
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
# In Use
from kivy.uix.popup import Popup

# Chef Bot Ingredient menu
__author__ = 'Alex Tejada'
#

kivyFile = 'main.kv'

class MainWindow(GridLayout):
    pass

class MenuPopup(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        return MainWindow()
    
    def Pressbtn(self, instance):
        request = instance.text
        print('[INFO   ] [Cobot App   ] Requesting ',request)
        show = MenuPopup()
        popupWindow = Popup(title="Requested " + request + '?', content=show , size_hint=(None, None), size=(400,400))
        popupWindow.open()
    
    def ConfirmSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + request + 'confirmed. ')
        popupWindow.dismiss()

        
    def DeclineSel(self, instance):
        print('[INFO   ] [Cobot App   ] Requested ' + request + 'cancelled. ')
        popupWindow.dismiss()


        # send request to Armando's part
        # get a reponse from the model 
        # send to Heidi's part 

    # Main Menu Color Decorators
    chef_bot_black = '2F3638'
    chef_bot_light = 'FEFFFE'
    chef_bot_gray = 'D6D6D6'
    chef_bot_primary = 'B3E0DB'
    chef_bot_secondary = 'DAE8D3'
    chef_bot_tertiary = 'F7F3E3'

    # Declarations
    request = ''
    popupWindow = object()

# End of app delcaration

if __name__ == "__main__":
    MainApp().run() 