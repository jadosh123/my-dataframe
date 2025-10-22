from series import Series
import pandas as pd
import numpy.testing as npt

int_arr = [1, 2, 3, 4]
float_arr = [1.0, 2.0, 3.0, 4.0]
int_dict = {'one': 1, 'two': 2, 'three': 3}
fl_int_dict = {'one': 1, 'two': 2, 'three': 3.0}


class TestSeries:

    def test_int_vals(self):
        npt.assert_array_equal(Series(int_arr).values,
                               pd.Series(int_arr).values)

    def test_int_lbls(self):
        npt.assert_array_equal(Series(int_arr).index,
                               pd.Series(int_arr).index)

    def test_float_vals(self):
        npt.assert_array_equal(Series(float_arr).values,
                               pd.Series(int_arr).values)

    def test_float_lbls(self):
        npt.assert_array_equal(Series(float_arr).index,
                               pd.Series(int_arr).index)

    def test_int_dict_vals(self):
        npt.assert_array_equal(Series(int_dict).values,
                               pd.Series(int_dict).values)

    def test_int_dict_lbls(self):
        npt.assert_array_equal(Series(float_arr).index,
                               pd.Series(int_arr).index)

    def test_slice(self):
        npt.assert_array_equal(Series(int_arr)[1:3].values,
                               pd.Series(int_arr)[1:3].values)

    def test_lbl_ind(self):
        assert Series(fl_int_dict)['two'] == pd.Series(fl_int_dict)['two']

    def test_int_ind(self):
        assert Series(float_arr)[2] == pd.Series(float_arr)[2]

    def test_out_int(self):
        assert print(Series(int_arr)) == print(pd.Series(int_arr))

    def test_out_dict(self):
        assert print(Series(fl_int_dict)) == print(pd.Series(fl_int_dict))
