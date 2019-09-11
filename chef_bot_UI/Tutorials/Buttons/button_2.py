# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Button with root

runTouchApp(Builder.load_string('''
Label:
    Button:
        text: 'B1'
        pos: root.x, root,top - self.height
    Button:
        text: 'B1'
        pos: root.right - self.width, root, root.y
'''))

