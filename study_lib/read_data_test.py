import pytest
import numpy as np
import pandas as pd

from study_lib.read_data import SML2010Data


def test_data_01_exists():
    # BUILD
    # OPERATE
    data = SML2010Data.new_data_1()

    # CHECK
    assert(data is not None)

def test_data_01_table():
    # BUILD
    # OPERATE
    data = SML2010Data.new_data_1()

    # CHECK
    assert(len(data) > 0)


def test_data_02_exists():
    # BUILD
    # OPERATE
    data = SML2010Data.new_data_2()

    # CHECK
    assert(data is not None)

def test_data_02_table():
    # BUILD
    # OPERATE
    data = SML2010Data.new_data_2()

    # CHECK
    assert(len(data) > 0)


def test_data_table():
    # BUILD
    # OPERATE
    data = SML2010Data.get_data()

    # CHECK
    assert(isinstance(data, pd.DataFrame))   


def test_data_shape():
    # BUILD
    # OPERATE
    data = SML2010Data.get_data()

    # CHECK
    assert(data.shape[0] == 4137)
    assert(data.shape[1] == 24)


def test_data_colnames():
    # BUILD
    # OPERATE
    data = SML2010Data.get_data()

    # CHECK
    np.testing.assert_array_equal(data.columns, SML2010Data.COLNAMES)