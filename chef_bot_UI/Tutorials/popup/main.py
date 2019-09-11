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

class Widgets(Widget):
    def btn(self):
        show_popup()

class MyApp(App):
    def build(self):
        return Widgets()

class MenuPopup(FloatLayout):
    pass

def show_popup():
    show = MenuPopup()
    popWin = Popup(title='dfdd', content=show, size_hint=(None, None), size=(400,400))
    popWin.open()

if __name__ == "__main__":
    MyApp().run()