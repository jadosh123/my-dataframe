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

    Raises\n
    ------
    KeyError\n
        If at least one key was request but none was found.
    """
    def __init__(self, parent_series):
        self._obj = parent_series

    def __getitem__(self, key: slice | str | int | list) -> Self | Any:
        if isinstance(key, slice):
            cls = type(self._obj)
            # Handle if slice is of type string
            start_pos = self._obj._lbl_dict.get(key.start)
            stop_pos = self._obj._lbl_dict.get(key.stop)

            # Check if valid labels
            if start_pos is None and key.start is not None:
                try:
                    start_pos = self._obj._lbl_dict.get(int(key.start))
                except (ValueError, TypeError):
                    pass
            if stop_pos is None and key.start is not None:
                try:
                    stop_pos = self._obj._lbl_dict.get(int(key.stop))
                except (ValueError, TypeError):
                    pass

            if start_pos is None and key.start is not None:
                raise KeyError(f"Label '{key.start}' was not found")
            if stop_pos is None and key.stop is not None:
                raise KeyError(f"Label '{key.stop}' was not found")

            stop_pos = stop_pos + 1 if stop_pos is not None else None

            int_slice = slice(start_pos, stop_pos, key.step)
            return cls(self._obj.values[int_slice], self._obj.index[int_slice])
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
        if ind is None:
            raise KeyError(
                f"The label you tried to access does not exist: {key}"
                )
        return self._obj.values[ind]
