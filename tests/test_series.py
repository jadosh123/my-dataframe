from series import Series
import pandas as pd
import numpy.testing as npt
import pytest

int_arr = [i for i in range(10)]
float_arr = [1.0, 2.0, 3.0, 4.0]
int_dict = {'one': 1, 'two': 2, 'three': 3}
fl_int_dict = {'one': 1, 'two': 2, 'three': 3.0}
trunc_arr = [i for i in range(100)]
nan_val_lbl = [[1, 2, None, 4], ['1', '2', '3', None]]


# Testing better design idea for refractoring later
@pytest.fixture
def my_nan_srs():
    return Series(nan_val_lbl[0], nan_val_lbl[1])


@pytest.fixture
def pd_nan_srs():
    return pd.Series(nan_val_lbl[0], nan_val_lbl[1])


class TestSeries:

    def test_int_vals(self):
        npt.assert_array_equal(Series(int_arr).values,
                               pd.Series(int_arr).values)

    def test_int_lbls(self):
        npt.assert_array_equal(Series(int_arr).index,
                               pd.Series(int_arr).index)

    def test_float_vals(self):
        npt.assert_array_equal(Series(float_arr).values,
                               pd.Series(float_arr).values)

    def test_float_lbls(self):
        npt.assert_array_equal(Series(float_arr).index,
                               pd.Series(float_arr).index)

    def test_int_dict_vals(self):
        npt.assert_array_equal(Series(int_dict).values,
                               pd.Series(int_dict).values)

    def test_int_dict_lbls(self):
        npt.assert_array_equal(Series(float_arr).index,
                               pd.Series(float_arr).index)

    def test_slice(self):
        npt.assert_array_equal(Series(int_arr)[1:3].values,
                               pd.Series(int_arr)[1:3].values)

    def test_lbl_ind(self):
        assert Series(fl_int_dict)['two'] == pd.Series(fl_int_dict)['two']

    def test_int_ind(self):
        assert Series(float_arr)[2] == pd.Series(float_arr)[2]

    def test_out_int(self):
        assert str(Series(int_arr)) == str(pd.Series(int_arr))

    def test_out_dict(self):
        assert str(Series(fl_int_dict)) == str(pd.Series(fl_int_dict))

    def test_iloc_int(self):
        assert (str(Series(int_arr).iloc[5]) ==
                str(pd.Series(int_arr).iloc[5]))

    def test_iloc_slice(self):
        assert (str(Series(int_arr).iloc[2:6]) ==
                str(pd.Series(int_arr).iloc[2:6]))

    def test_loc_lbl(self):
        assert (str(Series(fl_int_dict).loc['two']) ==
                str(pd.Series(fl_int_dict).loc['two']))

    def test_loc_list(self):
        assert (str(Series(int_arr).loc[[2, 3, 4, 4]]) ==
                str(pd.Series(int_arr).loc[[2, 3, 4, 4]]))

    def test_loc_slice(self):
        assert (str(Series(int_arr).loc[2:4]) ==
                str(pd.Series(int_arr).loc[2:4]))

    def test_loc_err(self):
        with pytest.raises(KeyError):
            Series(int_arr).loc[11]

    def test_nan_output(self, my_nan_srs, pd_nan_srs):
        assert (str(my_nan_srs) ==
                str(pd_nan_srs))

    def test_nan_lbl_val_types(self, my_nan_srs: Series,
                               pd_nan_srs: pd.Series):
        assert ([my_nan_srs.index.dtype, my_nan_srs.values.dtype] ==
                [pd_nan_srs.index.dtype, pd_nan_srs.values.dtype])

    def test_nan_addition(self, my_nan_srs: Series,
                          pd_nan_srs: pd.Series):
        npt.assert_array_equal((my_nan_srs + my_nan_srs).values, (pd_nan_srs + pd_nan_srs).values)

    def test_nan_addition_labels(self, my_nan_srs: Series,
                                 pd_nan_srs: pd.Series):
        npt.assert_array_equal((my_nan_srs + my_nan_srs).index, (pd_nan_srs + pd_nan_srs).index)







