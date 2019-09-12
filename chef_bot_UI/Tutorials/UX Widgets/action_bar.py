# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder


runTouchApp(Builder.load_string('''

ActionBar:
    pos_hint: {'top': 1}
    ActionView: 
        ActionPrevious:
            title: 'Chef Bots'
            with_previous: False
        ActionButton:
            text: 'Help'

'''))


