from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string('''

PageLayout:
    Button:
        text: 'B1'
    Button: 
        text: 'B2'  
    Button:
        text: 'B3'
'''))