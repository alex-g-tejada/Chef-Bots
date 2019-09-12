# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

# How to write a tex

text = """
Label:
    text: 
        ('[b]Hello[/b] Kitty\\n'
        '[u]Hello[/u] Kitty')
    font_size: '50'
    markup: True
"""
class Text(App):
    def build(self):
        return Builder.load_string(text)

if __name__ == "__main__":
    Text().run()


