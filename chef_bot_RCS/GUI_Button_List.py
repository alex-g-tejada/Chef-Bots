# 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class TestClass(App):
    def build(self):
        my_box = BoxLayout()
        my_show_list = ["Lettuce", "Tomato", "Onion", "Topping #"]
        my_box.my_buttons = [] # if you want to keep an "easy" reference to your buttons to do something with them later
                               #kivy doesnt crashes because it creates the property automatically
        for message in my_show_list:
            button = Button(text=message)
            my_box.my_buttons.append(button)
            my_box.add_widget(button)
        return my_box


if __name__ == "__main__":
    TestClass().run()