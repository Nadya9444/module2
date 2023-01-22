import os
import sys
import math
import pytest

sys.path.append(os.getcwd())
from main import sqrt


def test_sqrt_return_int():
    assert sqrt(4) == 2
    assert sqrt(9) == math.sqrt(9)
    assert sqrt(10000) == 100


def test_sqrt_return_float():
    assert round(sqrt(2), 13) == round(math.sqrt(2), 13)
    assert round(sqrt(3), 13) == round(math.sqrt(3), 13)
    assert round(sqrt(5), 13) == round(math.sqrt(5), 13)


def test_sqrt_receive_zero_return_zero():
    assert sqrt(0) == 0
    assert sqrt(0) == math.sqrt(0)


def test_sqrt_receive_negative_raise_value_error():
    with pytest.raises(ValueError):
        sqrt(-1)
        sqrt(-25)
        sqrt(-999999)


def test_sqrt_receive_alpha_raise_type_error():
    with pytest.raises(TypeError):
        sqrt('')
        sqrt('asdf')
        sqrt('some string')
