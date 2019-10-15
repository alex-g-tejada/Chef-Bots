# cobot_state.py
from cobot_states import ReceiveState


"""
This will act as the cobot control device that will hold one state to
control the cobot functionality
"""
class CobotControl(object):

    """
    Control constructor that will set the default state as the 
    ReceiveState to await new user input
    """
    def __init__(self):
        self.state = ReceiveState()
    
    """
    The control will pass the event to change the state if the proper
    event has occurred with the cooresponding state. Event will be the 
    state keys: string text from the main program.
    """
    def on_event(self, event):
        self.state = self.state.on_event(event)