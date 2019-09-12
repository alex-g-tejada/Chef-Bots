from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string('''

GridLayout:
    cols: 3
    padding: 40
    spacing: 10
    Button:
        text: 'B1'
    Button:
        text: 'B2'
    Button:
        text: 'B3'
    Button:
        text: 'B4'
    Button:
        text: 'B5'
    Button:
        text: 'B6'
    Button:
        text: 'B7'
    Button:
        text: 'B8'
'''))