from enum import Enum

class StateParser(Enum):
    NORMAL_STATE = 'normal_state'
    BACK_STATE = 'back_state'
    FINAL_STATE = 'final_state'
    ERROR_STATE = 'error_state'
    NONE = 'none'