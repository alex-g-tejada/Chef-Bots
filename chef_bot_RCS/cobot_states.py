# cobot_states.py
from state import State


"""
The Defualt State:


"""
class ReceiveState(State):
    def on_event(self, event):
        if event == 'Complete':
            return GatherImageState()
        return self

class GatherImageState(State):
    def on_event(self, event):
        if event == 'Ready':
            return ResponseState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class ResponseState(State):
    def on_event(self, event):
        if event == 'Not Found':
            return CancelOrderState()
        elif event == 'Found':
            return ToppingPointState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class ToppingPointState(State):
    def on_event(self, event):
        if event == 'Done':
            return ReceiveState()
        elif event == 'Error':
            return CancelOrderState()
        return self

class CancelOrderState(State):
    def on_event(self, event):
        if event == 'Finished':
            # Reset topping to default
            self.orderTopping = 'None'
            return ReceiveState
        return self 

