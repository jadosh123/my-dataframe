from typing import Any, Self
import operator


class _iLocIndexer:
    """
    Purely integer-location based indexing for selection by position.

    You can access specific values by their index or create a slice.
    """
    def __init__(self, parent_series):
        self._obj = parent_series

    def __getitem__(self, key: slice | int) -> Self | Any:
        if isinstance(key, slice):
            cls = type(self._obj)
            return cls(self._obj.values[key], self._obj.index[key])
        # If not slice return the specific value
        else:
            ind = operator.index(key)

        return self._obj.values[ind]


class _LocIndexer:
    """
    Access a group of rows and columns by label(s).

    You can access specific values by their label(s) or return a slice.
    """
    def __init__(self, parent_series):
        self._obj = parent_series

    def __getitem__(self, key: slice | str | int | list) -> Self | Any:
        if isinstance(key, slice):
            cls = type(self._obj)
            return cls(self._obj.values[key], self._obj.index[key])
        # If list of labels return a new series containing all the data
        elif isinstance(key, list):
            vals = []
            lbls = key
            for lbl in key:
                # Capture the index of each label and add the value to vals
                ind = self._obj._lbl_dict.get(lbl)
                vals.append(self._obj.values[ind])
            # Capture the class
            cls = type(self._obj)
            return cls(vals, lbls)

        # If key is a single label or int
        ind = self._obj._lbl_dict.get(key)
        return self._obj.values[ind]
