from utils.type_check import safe_type_cast
from collections.abc import Mapping
import pandas as pd

MAX_DISPLAY_VAL = 60


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
            keys = [i for i in range(len(values))]

        # Decide type and store ndarray
        arr = safe_type_cast(values, dtype=dtype)

        # Copy only if specified
        if copy:
            arr = arr.copy()

        # Store array and dtype
        self.values = arr
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
            indices = [i for i in range(len(self.values))]
            self.index = safe_type_cast(indices)
        return

    def __repr__(self):
        # Determine the longest label and value to print to calculate padding
        max_lbl_len = 0
        max_val_len = 0

        if len(self.index) <= MAX_DISPLAY_VAL:
            lbls = self.index
            vals = self.values
        else:
            # Grab first and last 5 elements from labels and values
            lbls = [*self.index[:5], *self.index[-5:]]
            vals = [*self.values[:5], *self.values[-5:]]

        for lbl, val in zip(lbls, vals):
            if len(f"{lbl}") > max_lbl_len:
                max_lbl_len = len(f"{lbl}")
            if len(f"{val}") > max_val_len:
                max_val_len = len(f"{val}")

        # Store max length +4 for white space
        max_length = max_lbl_len + max_val_len + 4

        # Add enough padding for uniform display of data
        if len(lbls) <= MAX_DISPLAY_VAL:
            res = [f"{lbl}" +
                   (max_length - len(f"{lbl}{val}"))*" " +
                   f"{val}\n"
                   for lbl, val in zip(lbls, vals)]
        else:
            # Construct the resulting string
            res = [f"{lbl}" +
                   (max_length - len(f"{lbl}{val}"))*" " +
                   f"{val}\n"
                   for lbl, val in zip(lbls, vals)]

        res.append(f"Length: {len(self.values)}, dtype: {self.dtype}")
        return "".join(res)


if __name__ == "__main__":
    temp = [i for i in range(61)]
    temp[30] = 50000000
    temp1 = pd.Series(temp)
    temp2 = Series(temp)
    print(temp1)
    print(temp2)
