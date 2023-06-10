from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    len_ = len(container)

    output = [0] * len_
    middle = [0] * (len_ + 1)

    for i in container:
        middle[i] += 1

    total = 0
    for i in range(len_ + 1):
        step = middle[i]
        middle[i] = total
        total += step

    for i in container:
        output[middle[i]] = i
        middle[i] += 1

    return output

    # TODO реализовать алгоритм сортировки подсчетами
