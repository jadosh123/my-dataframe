import pandas as pd
import numpy as np
from collections.abc import Collection


def type_checker(data: list):
    """
    A type checking function for the series, it returns the datatype.
    """
    # Most general type as placeholder until we determine the type
    data_types = set()

    for element in data:
        data_types.add(type(element))

    # Check wether we have any collection or string type
    if any((issubclass(t, Collection)) or 
           (t is str) for t in data_types):
        return np.object_
    elif float in data_types:
        # If bool and float exist then object is best
        if bool in data_types:
            return np.object_
        else:
            return np.float64
    elif int in data_types:
        return np.int64
    else:
        return np.bool


if __name__ == "__main__":
    tmp = [1, 'hello', 3, 4.5]
    tmp2 = pd.Series(['hello', 'test', 'hi'])
    dtype = type_checker(tmp)
    print(dtype)
    print(tmp2)