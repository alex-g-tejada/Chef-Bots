import kivy

# Version Selection
kivy.require("1.9.0")

# Load Kivy Modules
from kivy.app import App
from kivy.uix.button import Label

class HelloKivy(App):

    # Returns the application from the class
    def build(self):
        return Label(text="Hello")

# Create an instance of the class HelloKivy
hellokivy = HelloKivy()

# Start the object opertaion
hellokivy.run()