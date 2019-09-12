# Main Kivy application class
from kivy.app import App
# User Interface Components\
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string('''

BoxLayout:
    orientation: 'vertical'
    spacing: 10
    padding: 50
    Button:
        text: 'First Button'
    Button:
        text: 'Second Button' 

'''))