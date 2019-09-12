# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

# Button with super

class Controller(FloatLayout):
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        button = Button(
            text='Hello World',
            font_size=10,
            pos_hint={'x': .8 , 'y': .8},
            size_hint=(.1, .1),
            color=(.7, .7, 0, 1)
        )
        self.add_widget(button)
        button = Button(
            text='Hello World 2',
            font_size=10,
            pos_hint={'x': .4 , 'y': .9},
            size_hint=(.1, .1),
            color=(.7, .7, 0, 1)
        )
        self.add_widget(button)
    

class Controller2App(App):
    def build(self):
        return Controller()

if __name__ == "__main__":
    Controller2App().run()

