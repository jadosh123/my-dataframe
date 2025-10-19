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
            self.index = safe_type_cast(index)
        elif keys is not None:
            self.index = safe_type_cast(keys)
        else:
            # Generate indices from 0 to length-1
            indices = [i for i in range(len(self.data_array))]
            self.index = safe_type_cast(indices)
        return

    def __repr__(self):
        # Determine the longest label and value to print to calculate padding
        max_lbl_len = 0
        max_val_len = 0
        for lbl, val in zip(self.index, self.data_array):
            if len(f"{lbl}") > max_lbl_len:
                max_lbl_len = len(f"{lbl}")
            if len(f"{val}") > max_val_len:
                max_val_len = len(f"{val}")

        # Store max length +4 for white space
        max_length = max_lbl_len + max_val_len + 4
        res = ""

        # Add enough padding for uniform display of data
        for lbl, val in zip(self.index, self.data_array):
            padding_to_add = max_length - len(f"{lbl}{val}")
            res += f"{lbl}" + padding_to_add*" " + f"{val}\n"
        res += f"dtype: {self.dtype}"
        return res


if __name__ == "__main__":
    tmp = Series({(4, 5): 500, 4: 50000000000, 9.0: 'hi'})
    tmp2 = pd.Series({(4, 5): 50, 4: 50000000000, 9.0: 'hi'})
    # tmp3 = pd.Series([1, 2, 3, 4, 10])
    print(tmp2)
    print(tmp)
