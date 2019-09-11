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

mainWindow = '''
<MenuButton@Button>:
    markup: True
    background_color: (0,0,0,0)
    background_normal: ''
    back_color: (1, 0, 1, 1)
    border_radius: [18]
    size: (180,70)
    size_hint: (None, None)
    border_radius: [18]
    bold: True
    on_press: app.Pressbtn(self)
    canvas.before:
        Color:
            rgba: rgba('FF9F1C')
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: self.border_radius

<MenuPopup>:
    Label:
        id: Confirm
        text: 'Welcome'
        size_hint: 0.6, 0.2
        pos_hint: {"x": 0.2, "Top": 1}

        Button:
            text: 'You passed'
            size_hint: 0.8, 0.2
            pos_hint: {'x': 0.1, 'y': 0.1}

BoxLayout:
    orientation: 'vertical'

    GridLayout:
        cols: 1
        size_hint_y: .15
        canvas:
            Color:
                rgb: rgba('011627')
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'Chef Bots'
            color: rgba('FDFFFC')
            pos_hint_x: .15
            bold: True
        
    GridLayout:
        cols: 3
        padding: 40
        spacing: 30
        canvas:
            Color:
                rgb: rgba('FDFFFC')
            Rectangle:
                pos: self.pos
                size: self.size
        MenuButton:
            id: T
            text: 'Tomatos'
        MenuButton:
            id: L
            text: 'Lettuce'
        MenuButton:
            id: On
            text: 'Onions'
        MenuButton:
            id: C
            text: 'Cheese'
        MenuButton:
            id: P
            text: 'Pickles'
    
    GridLayout:
        cols: 1
        size_hint_y: .05
        canvas:
            Color:
                rgb: rgba('011627')
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: ''
            color: rgba('FDFFFC')
            pos_hint_x: .15
            bold: True

'''

confirmPopup = '''
FloatLayout:
    Label:
        id: Confirm
        text: 'Welcome'
        size_hint: 0.6, 0.2
        pos_hint: {"x": 0.2, "Top": 1}

        Button:
            text: 'You passed'
            size_hint: 0.8, 0.2
            pos_hint: {'x': 0.1, 'y': 0.1}
'''

class MainWindow(Widget):
    pass

class MenuPopup(FloatLayout):
    pass
    
class Menu2App(App):
    def build(self):
        runTouchApp(Builder.load_string(mainWindow))
        return MainWindow()
    
    def Pressbtn(self, instance):
        request = instance.text
        print('[INFO   ] [Cobot App   ] Requesting ',request)
        #show = confirmPopup
        #popupWindow = Popup(title="Popup Window", content=show , size_hint=(None, None), size=(400,400))
    
if __name__ == "__main__":
    Menu2App().run() 