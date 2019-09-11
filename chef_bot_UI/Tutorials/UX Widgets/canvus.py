# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
GridLayout:
    canvas:
        Color:
            rgb: rgba('F7FFF7')
        Rectangle:
            pos: self.pos
            size: self.size
'''))


