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
            text: 'Chef Bots'
            with_previous: False
        ActionButton:
            text: 'B1'
        ActionButton:
            text: 'B2'
        ActionGroup:
            text: 'Tools' 
            mode: 'spinner'
            color: .5, .5, 0, 1
            font_size: 13
            ActionButton:
                text: 'Tool1'
            ActionButton:
                text: 'Tool2'
            ActionButton:
                text: 'Tool3'
            ActionButton:
                text: 'Tool4'
'''))


