# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

# Labels with properties

kv = """
<Lab@Label>:
    size_hint_y: None
    height: dp(200)
    font_size: dp(70)
    text: 'Test'
    color: 1,2,0,45,1
    disabled_color: self.color
    disabled: True

BoxLayout: 
    orientation: 'vertical'
    Lab: 
        markup: False
    Lab: 
        markup: False
    Lab: 
        markup: False

"""

class Textdisabled(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    Textdisabled().run()


