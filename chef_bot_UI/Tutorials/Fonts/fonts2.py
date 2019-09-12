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

text_sample = """
Hey man da da da da da da da da da da da da da da
Hey man da da da da da da da da da da da da da da
Hey man da da da da da da da da da da da da da da

Hey man da da da da da da da da da da da da da da
Hey man da da da da da da da da da da da da da da
Hey man da da da da da da da da da da da da da da

Hey man da da da da da da da da da da da da da da

Hey man da da da da da da da da da da da da da da
Hey man da da da da da da da da da da da da da da

Hey man da da da da da da da da da da da da da da
Hey man da da da da da da da da da da da da da da
Hey man da da da da da da da da da da da da da da
Hey man da da da da da da da da da da da da da d
"""
class Text(App):
    def build(self):
        L = Label(
            text = text_sample,
            text_size=(300,None),
            line_height=1
        )
        return L

if __name__ == "__main__":
    Text().run()


