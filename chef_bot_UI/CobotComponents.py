from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget 
from kivy.uix.actionbar import ActionBar, ActionButton
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.properties import StringProperty, BooleanProperty


class CancelBtn(Button):
    
    #enabled = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(CancelBtn, self).__init__(*args, **kwargs)
        self.popupWindow = object()
        CancelBtn.disabled = False

    def on_enabled(self, value):
        if value:
            self.background_color = [1,1,1,1]
            self.color = [1,1,1,1]
            CancelBtn.disabled = value
        else:
            self.background_color = [1,1,1,.3]
            self.color = [1,1,1,.5]

    def on_touch_down(self, touch):
        
        if True == CancelBtn.disabled:
            #print('[INFO   ] [Cobot App   ] Cancel Button Push ', CancelBtn.disabled)
            self.on_press()
            return super(self.__class__, self).on_touch_down(touch)
    

"""
Screen to display individual set of ingredients
"""
class OneSelectScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

"""
Screen to allow the user to individually select the ingrients
the cobot should find
"""
class MultSelectScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

"""
Landing page for the application that will greet the user 
"""
class GreeterScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

"""
Popup Window for user confirmation of a topping
"""
class MenuPopup(FloatLayout):
    pass

class MenuPopup_Mult(FloatLayout):
    pass

class MenuPopup_Can(FloatLayout):
    pass

class MenuPopup_Error(FloatLayout):
    pass