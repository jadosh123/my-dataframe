import numpy as np


class Series():
    """
    A series class that is meant to mimic the pandas series
    and act as the building block of the final dataframe.

    A series is a One-dimensional ndarray with axis labels.
    """

    def __init__(self, data=None, index=None, dtype=None,
                 name=None, copy=None):
        if type(data) is type(dict()):
            # Lets store the keys and values seperately
            self.index_labels = list(data.keys())
            self.data_array = np.array(list(data.values()))


if __name__ == "__main__":
    test = int(56.3)
    print(type(test))
    print(test)