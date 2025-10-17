import numpy as np


def type_checker(data: list):
    """
    A type checking function for the series, it returns the datatype.
    """
    # Most general type as placeholder until we determine the type
    safest_type = object
    
    for element in data:
        if type(element)