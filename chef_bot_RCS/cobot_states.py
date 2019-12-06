from state import State
from threading import Thread
from ArmControl import arm_controller
from ult import Threadingclass
from cobot_cam import CameraModule
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

    def run_state(self, event=None):
        print('No action avaliable - ReceiveState')
        return None

class DetectionState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("[INFO   ] [Cobot RCS   ] [Dectection  ] Initializing camera...")
        self.camObject = CameraModule()
        self.imgdir="Images/"
        self.imgprefix="CapF"
        self.fullscreen=False
        self.detectXYZ=True
        self.calculateXYZ=True
        self.move_arm=False


    def run_state(self, orderList):
        try:
            # Camera setup code #
            print("[INFO   ] [Cobot RCS   ] [Dectection  ] List", orderList)
            self.camObject.capturefromPiCamera(self.imgdir,
                                               self.imgprefix,
                                               self.fullscreen,
                                               self.detectXYZ,
                                               self.calculateXYZ,
                                               self.move_arm)
            print("[INFO   ] [Cobot RCS   ] [Dectection  ] Done")
            return orderList
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
        self.imgdir="Images/"

    def run_state(self, orderList):
        try:
            # AI Code Here #
            result = []

            print("[INFO   ] [Cobot RCS   ] [Response    ] Done")
            return result
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
        # Communicate with Pi and Arduino
        #self.controller = arm_controller()

    def on_event(self, event):
        if event == 'Point Complete':
            return ReceiveState()
        elif event == 'Error':
            return CancelOrderState()
        return self
    
    def run_state(self, orderList):
        try:
            # Arm Code Here #
            result = orderList

            print("[INFO   ] [Cobot RCS   ] [PinPoint    ] Done") 
            return result
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

    def run_state(self, orderList):
        print('Running')
