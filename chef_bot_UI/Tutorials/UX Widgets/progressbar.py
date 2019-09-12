# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder


runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    ProgressBar:
        id: bar
        max: 100
        value: 10
'''))


