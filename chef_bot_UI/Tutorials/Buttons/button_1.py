# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string('''
Label:
    Button:
        text: 'B1'
        font_size: 32
        color: .8, .9, 0, 1
        size: 200, 200
        pos: 50, 100
    Button:
        text: 'B1'
        font_size: 34
        color: .2, .9, 0, 1
        size: 200, 200
        pos: 400, 100
'''))

