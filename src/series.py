from utils.type_check import safe_type_cast
from collections.abc import Mapping
import pandas as pd


class Series():
    """
    A series class that is meant to mimic the pandas series
    and act as the building block of the final dataframe.

    A series is a One-dimensional ndarray with axis labels.
    """

    def __init__(self, data=None, index=None, dtype=None,
                 name=None, copy=None):
        if data is None:
            keys = []
            values = []
        # If data argument is a Mapping
        elif isinstance(data, Mapping):
            keys = list(data.keys())
            values = list(data.values())
        # Iterable list like type
        else:
            values = list(data)

        # Decide type and store ndarray
        arr = safe_type_cast(values, dtype=dtype)

        # Copy only if specified
        if copy:
            arr = arr.copy()

        # Store array and dtype
        self.data_array = arr
        self.dtype = arr.dtype

        # If index specified
        if index is not None:
            # We need to make sure the lengths match
            if len(index) != len(keys):
                raise ValueError(
                    "Length of index does not match length of data"
                    )
            self.index_labels = index
        else:
            self.index_labels = keys
        return


if __name__ == "__main__":
    tmp = Series({'test': 5})
    tmp2 = pd.Series({'test': 5})
    print(tmp.data_array)
    print(tmp.index_labels)
    print(tmp.dtype)
    print(tmp2.dtype)
