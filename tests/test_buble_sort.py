import os
import sys

sys.path.append(os.getcwd())
from main import bubble_sort, bubble_sort_on_first_arg_in_tuple


def test_bubble_sort_with_one_arg():
    assert bubble_sort([1]) == [1]


def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []


def test_bubble_sort_of_int():
    assert bubble_sort([2, 3, 1, 4]) == [1, 2, 3, 4]


def test_bubble_sort_of_alpha_():
    assert bubble_sort(['a', 'c', 'b', 'z', 'm', 'x']) == ['a', 'b', 'c', 'm', 'x', 'z']


def test_bubble_sort_stable():
    assert bubble_sort_on_first_arg_in_tuple(
        [(1, 0), (2, 1), (1, 2)]
    ) == [(1, 0), (1, 2), (2, 1)]
    assert bubble_sort_on_first_arg_in_tuple(
        [(4, 0), (1, 1), (4, 2), (1, 3), (4, 4), (2, 5), (0, 6), (-10, 7)]
    ) == [(-10, 7), (0, 6), (1, 1), (1, 3), (2, 5), (4, 0), (4, 2), (4, 4)]
