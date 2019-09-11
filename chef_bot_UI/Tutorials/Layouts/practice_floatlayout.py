# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string('''
<Button>:
    color: .4, .7, 0, 1
    front_size: 300
    size_hint: .3, .2

FloatLayout:
    Button:
        text: 'B1'
        pos_hint: {'x': 0, 'top': 1}
    Button:
        text: 'B2'
        pos_hint: {'y': 0, 'right': 1}  


'''))

