import operator
from collections.abc import Callable, Mapping
from typing import Any, Self

import numpy as np

# # For quick testing
import pandas as pd
from numpy.typing import NDArray

from my_dataframe.utils.indexing import _iLocIndexer, _LocIndexer
from my_dataframe.utils.type_check import change_none, safe_type_cast

MAX_DISPLAY_VAL = 60
SENTINEL_NONE = "__INDEX_NONE_SENTINEL__"


class Series:
    """A series class that is meant to mimic the pandas series
    and act as the building block of the final dataframe.

    A series is a One-dimensional ndarray with axis labels.
    """

    def __init__(
        self,
        data: Mapping | list[Any] | NDArray[Any] | None = None,
        index: list[Any] | NDArray[Any] | None = None,
        dtype: Any | None = None,
        name: str | None = None,
        copy: bool | None = None,
    ):
        if data is None or len(data) == 0:
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

        # Convert none to np.nan then coerce values to appropraite type
        change_none(values)
        arr = safe_type_cast(values, dtype=dtype)

        # Copy only if specified
        if copy:
            arr = arr.copy()

        # Store array and dtype
        self.values = arr

        # If index specified
        if index is not None:
            # We need to make sure the lengths match
            if len(index) != len(keys):
                raise ValueError("Length of index does not match length of data")
            self.index = safe_type_cast(index)
        elif keys is not None:
            self.index = safe_type_cast(keys)
        else:
            # Generate indices from 0 to length-1
            indices = [i for i in range(len(self.values))]
            self.index = safe_type_cast(indices)

        # Store indices with labels in a dictionary for O(1) access
        self._lbl_dict = {lbl: i for lbl, i in zip(self.index, range(len(self.index)))}

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
            lbls = [
                *[str(lbl) for lbl in self.index[:5]],
                "  ",
                *[str(lbl) for lbl in self.index[-5:]],
            ]

            vals = [
                *[str(val) for val in self.values[:5]],
                "...",
                *[str(val) for val in self.values[-5:]],
            ]

        # Calculate the longest values for padding
        max_lbl_len = max(len(lbl) for lbl in lbls)
        max_val_len = max(len(val) for val in vals)

        # Store max length +4 for white space
        max_length = max_lbl_len + max_val_len + 4

        # Construct the result
        res = [
            f"{lbl}"
            + (max_length - len(f"{lbl}{val}")) * " "
            + ("NaN\n" if val == "nan" else f"{val}\n")
            for lbl, val in zip(lbls, vals)
        ]

        # Check if to include length for truncated output
        if len(self.index) <= MAX_DISPLAY_VAL:
            res.append(f"dtype: {self.dtype}")
        else:
            res.append(f"Length: {len(self.index)}, dtype: {self.dtype}")

        return "".join(res)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key: slice | str | int) -> Self | Any:
        if isinstance(key, slice):
            cls = type(self)
            return cls(self.values[key], self.index[key])
        if isinstance(key, str):
            # Here we need to get the index of the label and
            # fetch the value at that index
            ind = self._lbl_dict.get(key)
        # If not slice return the specific value
        else:
            ind = operator.index(key)

        return self.values[ind]

    def _arith_op(
        self, other: Self, op: Callable[[np.ndarray, np.ndarray], np.ndarray]
    ) -> Self:
        # We need to convert the array to compatible types before addition and sorting with numpy union1d
        normalized_self_index = self._normalize_index(self.index)
        normalized_other_index = self._normalize_index(other.index)

        # Created master index array for final output
        master_label = np.union1d(normalized_self_index, normalized_other_index)

        # Now we need to find the indices in the orginal series that match the master index
        master_indices1 = np.searchsorted(master_label, self.index)
        master_indices2 = np.searchsorted(master_label, other.index)

        # Now we create two identical length ndarrays of NaNs
        master_values1 = np.array(object=[np.nan for _ in range(len(master_label))])
        master_values2 = np.array(object=[np.nan for _ in range(len(master_label))])

        # And finally fill the values in their respective indices and return a new instance of the class
        np.put(master_values1, master_indices1, self.values)
        np.put(master_values2, master_indices2, other.values)
        master_values = op(master_values1, master_values2)

        # Revert the sentinel to None
        master_label[master_label == SENTINEL_NONE] = None

        cls = type(self)
        return cls(data=master_values, index=master_label)

    def __add__(self, other: Self | Any) -> Self:
        return self._arith_op(other, operator.add)

    def __sub__(self, other: Self | Any) -> Self:
        return self._arith_op(other, operator.sub)

    def __mul__(self, other: Self | Any) -> Self:
        return self._arith_op(other, operator.mul)

    def __truediv__(self, other: Self | Any) -> Self:
        return self._arith_op(other, operator.truediv)

    def _normalize_index(self, idx: np.ndarray) -> np.ndarray:
        """Temporarily replaces None in the index array with a string sentinel"""
        temp_idx = np.asanyarray(idx, dtype=object)
        temp_idx[temp_idx == None] = SENTINEL_NONE
        return temp_idx

    # Dynamic attributes
    @property
    def iloc(self):
        return _iLocIndexer(self)

    @property
    def loc(self):
        return _LocIndexer(self)

    @property
    def size(self):
        return len(self.values)

    @property
    def empty(self):
        return True if len(self.values) == 0 else False

    @property
    def dtype(self):
        return self.values.dtype

    @property
    def dtypes(self):
        return self.dtype


if __name__ == "__main__":
    nan_val_lbl = [[1, 2, None, 4], ["1", "2", "3", None]]
    test = pd.Series(data=nan_val_lbl[0], index=nan_val_lbl[1])
    test1 = Series(data=nan_val_lbl[0], index=nan_val_lbl[1])
    print(test / test)
    print(test1 / test1)
