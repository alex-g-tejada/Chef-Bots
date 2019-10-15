from state import State


"""
The Defualt State:


"""
class ReceiveState(State):
    def on_event(self, event):
        if event == 'Request Confirmed':
            return DetectionState()
        return self

class DetectionState(State):
    def on_event(self, event):
        if event == 'Setup Complete':
            return ResponseState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class ResponseState(State):
    def on_event(self, event):
        if event == 'Not Found':
            return CancelOrderState()
        elif event == 'Found':
            return PinPointState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class PinPointState(State):
    def on_event(self, event):
        if event == 'Point Complete':
            return ReceiveState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class CancelOrderState(State):
    def on_event(self, event):
        if event == 'Request Completed':
            # Reset topping to default
            self.orderTopping = 'None'
            return ReceiveState
        return self 

