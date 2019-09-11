# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder


runTouchApp(Builder.load_string('''
GridLayout:
    cols: 2
    CheckBox:
        active: False
    Label:
        text: 'ch1'
    CheckBox:
        active: True
    Label:
        text: 'ch2'
    CheckBox:
        group: 'Radio Button'
        active: True
    Label:
        text: 'radi bu'
    
'''))


