from utils.typing import type_checker
import pandas as pd


class TestClass:
    def test_type_int(self):
        tmp = [1, 2, 3]
        assert type_checker(tmp) == pd.Series(tmp).dtype.type

    def test_type_bool(self):
        tmp = [True, False, True]
        assert type_checker(tmp) == pd.Series(tmp).dtype.type

    def test_type_float(self):
        tmp = [3.5, 1.5, 5]
        assert type_checker(tmp) == pd.Series(tmp).dtype.type

    def test_type_object(self):
        tmp = ['hello', 2, [1], 4.5, {"hi": 4}]
        assert type_checker(tmp) == pd.Series(tmp).dtype.type

    def test_type_float_bool(self):
        tmp = [4.5, 5, True]
        assert type_checker(tmp) == pd.Series(tmp).dtype.type
