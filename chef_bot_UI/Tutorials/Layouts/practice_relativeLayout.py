from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string('''

RelativeLayout:
 
    Button:
        text: 'B1'
        size_hint: .4, .4
        pos: 20, 100
    Button:
        text: 'B2'
        size_hint: .5, .5
        size_hint: .2, .2
    
'''))