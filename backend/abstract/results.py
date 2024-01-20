from enum import Enum


class Results(Enum):
    NONE = "None"
    PASS = "Pass"
    FAIL = "Fail"
    PARTIAL_FAILURE = "Partial Failure"
    SCRIPT_ERROR = "Script"
    CONFIGURATION = "Configuration"
