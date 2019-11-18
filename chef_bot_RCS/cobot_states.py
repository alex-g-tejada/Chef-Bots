from state import State
from threading import Thread
from ult import Threadingclass
import time


"""
The Defualt State: ReceoveState



"""
class ReceiveState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("[INFO   ] [Cobot RCS   ] [Receive     ] Initializing cobot...")
        print("[INFO   ] [Cobot RCS   ] [Receive     ] Ready for new request")

    def on_event(self, event):
        if event == 'Request Confirmed':
            return DetectionState()
        return self

    def run_state(self):
        print('No action avaliable - ReceiveState')

class DetectionState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("[INFO   ] [Cobot RCS   ] [Dectection  ] Initializing camera...")
    
        #self.run_state()

    def run_state(self):
        try:
            # Camera setup code #


            print("[INFO   ] [Cobot RCS   ] [Dectection  ] Done")
        except:
            print("[INFO   ] [Cobot RCS   ] [Dectection  ] Camera could not initalize")


    def on_event(self, event):
        if event == 'Setup Complete':
            return ResponseState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class ResponseState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("[INFO   ] [Cobot RCS   ] [Response    ] Analyzing request...")

    def run_state(self):
        try:
            # AI Code Here #


            print("[INFO   ] [Cobot RCS   ] [Response    ] Done")
        except:
            print("[INFO   ] [Cobot RCS   ] [Response    ] Could not analyze order")



    def on_event(self, event):
        if event == 'Not Found':
            return CancelOrderState()
        elif event == 'Found Request':
            return PinPointState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class PinPointState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("[INFO   ] [Cobot RCS   ] [PinPoint    ] Moving arm...")

    def on_event(self, event):
        if event == 'Point Complete':
            return ReceiveState()
        elif event == 'Error':
            return CancelOrderState()
        return self
    
    def run_state(self):
        try:
            # Arm Code Here #
            #armControl = arm_controller()

            print("[INFO   ] [Cobot RCS   ] [PinPoint    ] Done")
        except:
            print("[INFO   ] [Cobot RCS   ] [PinPoint    ] Could not communicate with arm")


class CancelOrderState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def on_event(self, event):
        if event == 'Request Completed':
            # Reset topping to default
            return ReceiveState
        return self

    def run_state(self):
        print('Running')
