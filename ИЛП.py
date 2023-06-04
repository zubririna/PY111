"""
This module implements some functions based on linear search algo
"""

from typing import List
from math import inf

def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве
    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """

    if len(arr) == 0:
        raise ValueError("Пустая последовательность")
    min_ind, min_val = None, inf
    for ind, val in enumerate(arr):
        if val < min_val:
            min_val, min_ind = val, ind
    return min_ind


