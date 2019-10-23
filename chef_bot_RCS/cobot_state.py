# cobot_state.py
from cobot_states import ReceiveState


"""
This will act as the cobot control device that will hold one state to
control the cobot functionality
"""
class CobotControl(object):

    """
    Control constructor that will set the default state as the 
    ReceiveState to await new user input. The controller defines
    the available states in the state machine as well as the keys
    to move one state to another
    """
    def __init__(self):
        self.state = ReceiveState()
        # States
        self.RS = "ReceiveState"
        self.DS = "DetectionState"
        self.SS = "ResponseState"
        self.PS = "PinPointState"
        self.CS = "CancelOrderState"
        # State Keys
        self.RC = 'Request Confirmed'
        self.SC = 'Setup Complete'
        self.ER = 'Error'
        self.NF = 'Not Found'
        self.FR = 'Found Request'
        self.PC = 'Point Complete'
        self.FC = 'Request Completed'
    
    """
    The control will pass the event to change the state if the proper
    event has occurred with the cooresponding state. Event will be the 
    state keys: string text from the main program.
    """
    def on_event(self, event):
        self.state = self.state.on_event(event)