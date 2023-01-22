import os
import sys
import pytest

sys.path.append(os.getcwd())
from main import quadratic_equation


def test_quadratic_equation_return_result():
    """ With real roots"""
    assert quadratic_equation(1, -70, 600) == (60, 10)


def test_quadratic_equation_return_one_root():
    """ With one real root"""
    assert quadratic_equation(3, -18, 27) == (3, None)


def test_quadratic_equation_return_none():
    """ Without real roots """
    assert quadratic_equation(1, 1, 1) == (None, None)


def test_quadratic_equation_receive_zero_a_argument_raise_zero_division():
    with pytest.raises(ZeroDivisionError):
        quadratic_equation(0, 1, 2)


def test_quadratic_equation_receive_alpha_raise_type_error():
    with pytest.raises(TypeError):
        quadratic_equation('some', 'string', '1')




