# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

# How to connect labels with buttons

runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    size_hint_y: None
    height: sp(300)
    Label:
        text: 'Hello'
        color: .9, .3, 0, 1
    Button:
        text: 'World'
'''))


