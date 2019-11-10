from state import State
from ArmControl import arm_controller
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


class DetectionState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("[INFO   ] [Cobot RCS   ] [Dectection  ] Initializing camera...")
        print("[INFO   ] [Cobot RCS   ] [Dectection  ] Done")
        #self.run_state()
    
    def run_state(self, event):
        print("Initalize Camera")
        return True

    
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
        print("[INFO   ] [Cobot RCS   ] [Response    ] Done")
        #time.sleep(5)
        # AI Code Here #


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
	armControl = arm_controller()
        print("[INFO   ] [Cobot RCS   ] [PinPoint    ] Done")
        # Arm Code Here #
    
    def on_event(self, event):
        if event == 'Point Complete':
            return ReceiveState()
        elif event == 'Error':
            return CancelOrderState()
        return self


class CancelOrderState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def on_event(self, event):
        if event == 'Request Completed':
            # Reset topping to default
            return ReceiveState
        return self 

