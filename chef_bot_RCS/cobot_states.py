from state import State


"""
The Defualt State: ReceoveState



"""
class ReceiveState(State):
    def on_event(self, event):
        if event == 'Request Confirmed':
            return DetectionState()
        return self


class DetectionState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        print("code start up!!")
        # AI Code Here #


    def on_event(self, event):
        if event == 'Not Found':
            return CancelOrderState()
        elif event == 'Found':
            return PinPointState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class PinPointState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("code start up!!")
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

