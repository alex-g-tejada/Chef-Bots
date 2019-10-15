# Basic State of the cobot 

"""
This state object will provide utility functions for the individual
states within the cobot state machine
"""
class State(object):
    # Topping Requesteed
    orderTopping = "None"
    
    """
    state constructor that will activate when a new state has been 
    given to the overall state.
    """
    def __init__ (self):
        print('[INFO   ] [Cobot RCS   ] Current State:  ', str(self))
    
    """
    Provides the current state name that will notify the user the phase 
    of the cobot.
    """
    def __str__ (self):
        return self.__class__.__name__
    
    """
    Leverages the _str- method to describe the State.
    """
    def __repr__ (self):
        return self.__str__()

    """
    Handle events that are delegated to this State.
    """
    def on_event(self, event):
        pass

    """
    State handler that will preform a specfic action
    """
    def run_state(self, event):
        pass