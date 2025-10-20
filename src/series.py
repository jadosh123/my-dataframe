from utils.type_check import safe_type_cast
from collections.abc import Mapping
import pandas as pd
import operator

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

        # Store private mapping for fast lookups
        # TODO before anything read about decarotors/usage and implementation
        # self._

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

        # Check if below truncation threshold
        if len(self.index) <= MAX_DISPLAY_VAL:
            lbls = [str(lbl) for lbl in self.index]
            vals = [str(val) for val in self.values]
        else:
            # Grab first and last 5 elements from labels and values
            lbls = [*[str(lbl) for lbl in self.index[:5]],
                    "  ",
                    *[str(lbl) for lbl in self.index[-5:]]]

            vals = [*[str(val) for val in self.values[:5]],
                    "...",
                    *[str(val) for val in self.values[-5:]]]

        # Calculate the longest values for padding
        max_lbl_len = max(len(lbl) for lbl in lbls)
        max_val_len = max(len(val) for val in vals)

        # Store max length +4 for white space
        max_length = max_lbl_len + max_val_len + 4

        # Construct the result
        res = [f"{lbl}" +
               (max_length - len(f"{lbl}{val}"))*" " +
               f"{val}\n"
               for lbl, val in zip(lbls, vals)]

        # Check if to include length for truncated output
        if len(self.index) <= MAX_DISPLAY_VAL:
            res.append(f"dtype: {self.dtype}")
        else:
            res.append(f"Length: {len(self.index)}, dtype: {self.dtype}")

        return "".join(res)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self.values[key], self.index[key])
        # elif isinstance(ind, str):

        # If not slice return the specific value
        index = operator.index(key)
        return self.values[index]


if __name__ == "__main__":
    # temp = {f"hello{i}": i for i in range(100)}
    # temp1 = pd.Series(temp)
    # temp2 = Series(temp)
    # temp1['hello1'] = 440000
    tempo = Series(data=[1, 2, 3, 4], index=['Hello', '2', '3', '4'])
    print(tempo[:2])
