# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# Apply touch library
from kivy.base import runTouchApp
# Text to application build
from kivy.lang import Builder
from functools import partial

Builder.load_string("""
<BoxLayout>:
    Button:
        text: 'Onions'
        size_hint: 0.2, 0.2
        pos_hint: {'x': .2, 'y': .3}
    Button: 
        text: 'Tomatos'
        size_hint: 0.2, 0.2
    Button:
        text: 'Lettuce'
        size_hint: 0.2, 0.2
    Button:
        text:'Box 4'
""")

class Chef_Bot_UI_Dev(App):
    
    def buttonDisable(self, instance, *args):
        instance.disabled = True
    def buttonUpdate(self, instance, *args):
        instance.text = "I am Disabled!"
    def build(self):
        #return Label(text="Hello Kivy!")
        #opLabel = Label(text="Menu", front_size='20')
        mainbtn = Button(text="Click to disable",
                  pos=(300,350),
                  size_hint=(.25, .18))
        mainbtn.bind(on_press=partial(self.buttonDisable,mainbtn))
        mainbtn.bind(on_press=partial(self.buttonUpdate, mainbtn))
        return buttonLayoutComponenet

# Example 3
class Controller(BoxLayout):
    def __init__ (self, **kwargs):
        super(Controller, self).__init__(**kwargs)

        button = Button(text='yes')
        self.add_widget(button)

class Class2(App):
    def build(self):
        return Controller

class MyList(BoxLayout):
    pass

if __name__ == '__main__':
    Class2().run()
    #Chef_Bot_UI_Dev().run()