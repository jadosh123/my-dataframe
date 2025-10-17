import numpy as np
from collections.abc import Mapping


class Series():
    """
    A series class that is meant to mimic the pandas series
    and act as the building block of the final dataframe.

    A series is a One-dimensional ndarray with axis labels.
    """

    def __init__(self, data=None, index=None, dtype=None,
                 name=None, copy=None):
        # If data argument is a dictionary
        if isinstance(data, Mapping):
            keys = list(data.keys())
            values = list(data.values())
            print("hello")

            # Respect selected dtype
            if dtype:
                arr = np.asarray(values, dtype=dtype)

            if copy:
                arr = arr.copy()

            self.data_array = arr

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
    test = int(56.3)
    print(type(test))
    print(test)