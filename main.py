import math


def sqrt(num: float) -> float:
    if num == 0:
        return 0
    elif num < 0:
        raise ValueError('math domain error')
    a = float(num)
    for i in range(500):
        num = 0.5 * (num + a / num)
    return num


def quadratic_equation(a: float, b: float, c: float) -> tuple:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = None
    else:
        return None, None
    return x1, x2


def bubble_sort(array: list) -> list:
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


def bubble_sort_on_first_arg_in_tuple(array: list) -> list:
    """Only for stable test"""
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j][0] > array[j + 1][0]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


def shell_sort(array: list) -> list:
    n = len(array)
    if n == 0:
        return []
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return array


def shell_sort_on_first_arg_in_tuple(array: list) -> list:
    """Only for stable test"""
    n = len(array)
    if n == 0:
        return []
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval][0] > temp[0]:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return array
