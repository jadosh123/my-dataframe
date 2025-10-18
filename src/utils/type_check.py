import pandas as pd
import numpy as np
from numpy.typing import NDArray, DTypeLike
from typing import Any
from collections.abc import Collection


def type_checker(data: list[Any]) -> DTypeLike:
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


def safe_type_cast(data: list[Any],
                   dtype: DTypeLike | None = None) -> NDArray[Any]:
    """
    Attempts to safely coerce the data inside the provided
    series to the specified type, in case of failure it defaults
    to most generic type `numpy.object_`.

    If dtype is specified it attempts to coerce the data to
    the specified type.
    """

    try:
        # Try coercing the data to the specified type
        if dtype:
            arr = np.asarray(data, dtype=dtype)
        else:
            dtype = type_checker(data)
            arr = np.asarray(data, dtype=dtype)
    except ValueError:
        # In case of value error default to generic type
        arr = np.asarray(data, dtype=np.object_)

    return arr


if __name__ == "__main__":
    tmp = [1, 'hello', 3, 4.5]
    tmp2 = pd.Series(['hello', 'test', 'hi'])
    dtype = type_checker(tmp)
    print(dtype)
    print(tmp2)
