from state import State
from threading import Thread
from ArmControl import arm_controller
from ult import Threadingclass
from cobot_cam import CameraModule
from camera_realworldxyz import camera_realtimeXYZ
import time
import os
import cv2


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
            self.camObject = []
            return orderList
        except:
            print("[INFO   ] [Cobot RCS   ] [Dectection  ] Camera could not initalize")
            error = "Could not setup detection"

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
        self.xyzcal = camera_realtimeXYZ()

    def run_state(self, orderList):
        #try:
            # AI Code Here #
            results = []
            path = "../chef_bot_RCS/Images/"
            tensorflowNet_onions = cv2.dnn.readNetFromTensorflow('models/onions.pb', 'output.pbtxt')
            print(path)
            for image in os.listdir(path):
                img = cv2.imread('image.jpg')
                rows, cols, channels = img.shape
                tensorflowNet_onions.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
                # Runs a forward pass to compute the net output
                networkOutput = tensorflowNet_onions.forward()
                for detection in networkOutput[0,0]:
                    score = float(detection[2])
                    if score > 0.9:
                        pic, XYZ = self.xyzcal(image, True)
                        results.append(XYZ)

            print("[INFO   ] [Cobot RCS   ] [Response    ] Done")
            return results
        #except:
            #print("[INFO   ] [Cobot RCS   ] [Response    ] Could not analyze order")


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
        self.controller = arm_controller()

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
            inputarr = [30,12,6,0,0,0]
            self.controller.move_untildone(inputarr)

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


if __name__ == "__main__":  
    Ai = ResponseState()
    lists = ["T","o"]
    results = Ai.run_state(lists)