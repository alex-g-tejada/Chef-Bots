# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

# How to create labels

class Controller2App(App):
    def build(self):
        return Label(text='[color=3333ff]Hello[/color] [color=333aaf]World[/color]', markup= True,
        font_size='60sp')

if __name__ == "__main__":
    Controller2App().run()

