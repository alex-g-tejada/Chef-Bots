from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string('''

AnchorLayout:
    anchor_x: 'left'
    anchor_y: 'bottom'
    Button:
        text: 'B1'
        size_hint: 0.5, 0.5
    Button:
        text: 'B2'
        size_hint: 0.2, 0.3


'''))