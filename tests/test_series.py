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
def my_nan_srs() -> Series:
    return Series(nan_val_lbl[0], nan_val_lbl[1])

@pytest.fixture
def pd_nan_srs() -> pd.Series:
    return pd.Series(nan_val_lbl[0], nan_val_lbl[1])

@pytest.fixture
def my_int_srs() -> Series:
    return Series(int_arr)

@pytest.fixture
def pd_int_srs() -> pd.Series:
    return pd.Series(int_arr)

@pytest.fixture
def my_float_srs() -> Series:
    return Series(float_arr)

@pytest.fixture()
def pd_float_srs() -> pd.Series:
    return pd.Series(float_arr)

@pytest.fixture()
def my_int_dict() -> Series:
    return Series(int_dict)

@pytest.fixture()
def pd_int_dict() -> pd.Series:
    return pd.Series(int_dict)

@pytest.fixture()
def my_flint_dict() -> Series:
    return Series(fl_int_dict)

@pytest.fixture()
def pd_flint_dict() -> pd.Series:
    return pd.Series(fl_int_dict)

class TestSeries:

    def test_int_vals(self, my_int_srs, pd_int_srs):
        npt.assert_array_equal(my_int_srs, pd_int_srs) 

    def test_int_lbls(self, my_int_srs, pd_int_srs):
        npt.assert_array_equal(my_int_srs, pd_int_srs)

    def test_float_vals(self, my_float_srs, pd_float_srs):
        npt.assert_array_equal(my_float_srs, pd_float_srs)

    def test_float_lbls(self, my_float_srs, pd_float_srs):
        npt.assert_array_equal(my_float_srs, pd_float_srs)

    def test_int_dict_vals(self, my_int_dict, pd_int_dict):
        npt.assert_array_equal(my_int_dict, pd_int_dict)

    def test_int_dict_lbls(self, my_int_dict, pd_int_dict):
        npt.assert_array_equal(my_int_dict, pd_int_dict)

    def test_slice(self, my_int_srs, pd_int_srs):
        npt.assert_array_equal(my_int_srs, pd_int_srs)

    def test_lbl_ind(self, my_flint_dict, pd_flint_dict): 
        assert my_flint_dict['two'] == pd_flint_dict['two'] 
    
    def test_int_ind(self, my_float_srs, pd_float_srs): 
        assert my_float_srs[2] == pd_float_srs[2]

    def test_out_int(self, my_int_srs, pd_int_srs):
        assert str(my_int_srs) == str(pd_int_srs)

    def test_iloc_int(self, my_int_srs, pd_int_srs):
        assert (str(my_int_srs.iloc[5]) == str(pd_int_srs.iloc[5]))

    def test_iloc_slice(self, my_int_srs, pd_int_srs):
        assert (str(my_int_srs.iloc[2:6]) == str(pd_int_srs.iloc[2:6]))

    def test_loc_lbl(self, my_flint_dict, pd_flint_dict):
        assert (str(my_flint_dict.loc['two']) == str(pd_flint_dict.loc['two']))

    def test_loc_list(self, my_int_srs, pd_int_srs):
        assert (str(my_int_srs.loc[[2, 3, 4, 4]]) ==
                str(pd_int_srs.loc[[2, 3, 4, 4]]))

    def test_loc_slice(self, my_int_srs, pd_int_srs):
        assert (str(my_int_srs.loc[2:4]) ==
                str(pd_int_srs.loc[2:4]))

    def test_loc_err(self, my_int_srs):
        with pytest.raises(KeyError):
            my_int_srs.loc[11]

    def test_nan_output(self, my_nan_srs, pd_nan_srs):
        assert (str(my_nan_srs) == str(pd_nan_srs))

    def test_nan_lbl_val_types(self, my_nan_srs: Series,
                               pd_nan_srs: pd.Series):
        assert ([my_nan_srs.index.dtype, my_nan_srs.values.dtype] ==
                [pd_nan_srs.index.dtype, pd_nan_srs.values.dtype])

    def test_nan_addition(self, my_nan_srs: Series,
                          pd_nan_srs: pd.Series):
        npt.assert_array_equal((my_nan_srs + my_nan_srs).values, (pd_nan_srs + pd_nan_srs).values)

    def test_nan_mult(self, my_nan_srs: Series,
                          pd_nan_srs: pd.Series):
        npt.assert_array_equal((my_nan_srs * my_nan_srs).values, (pd_nan_srs * pd_nan_srs).values)

    def test_nan_truediv(self, my_nan_srs: Series,
                          pd_nan_srs: pd.Series):
        npt.assert_array_equal((my_nan_srs / my_nan_srs).values, (pd_nan_srs / pd_nan_srs).values)

    def test_nan_addition_labels(self, my_nan_srs: Series,
                                 pd_nan_srs: pd.Series):
        npt.assert_array_equal((my_nan_srs + my_nan_srs).index, (pd_nan_srs + pd_nan_srs).index)

    def test_nan_mult_labels(self, my_nan_srs: Series,
                                 pd_nan_srs: pd.Series):
        npt.assert_array_equal((my_nan_srs * my_nan_srs).index, (pd_nan_srs * pd_nan_srs).index)

    def test_nan_truediv_labels(self, my_nan_srs: Series,
                                 pd_nan_srs: pd.Series):
        npt.assert_array_equal((my_nan_srs / my_nan_srs).index, (pd_nan_srs / pd_nan_srs).index)

  





