from series import Series
import pandas as pd
import numpy.testing as npt

int_sr = [1, 2, 3, 4]
float_sr = [1.0, 2.0, 3.0, 4.0]
fl_int_sr = [1, 2.3, 4, 6]
int_dict = {'one': 1, 'two': 2, 'three': 3}
fl_int_dict = {'one': 1, 'two': 2, 'three': 3.0}


class TestSeries:

    def test_int_vals(self):
        npt.assert_array_equal(Series(int_sr).values, pd.Series(int_sr).values)

    def test_int_lbls(self):
        npt.assert_array_equal(Series(int_sr).index, pd.Series(int_sr).index)
