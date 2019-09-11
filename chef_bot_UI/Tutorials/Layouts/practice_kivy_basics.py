# Main Kivy application class
from kivy.app import App
# User Interface Components
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Class1(BoxLayout):
    def __init__(self, **kwargs):
        super(Class1, self).__init__(**kwargs)
        self.padding = 50
        button = Button(text='Hey')
        self.add_widget(button)

class Class2(App):
    def build(self):
        return Class1()

if __name__ == "__main__":
    Class2().run()