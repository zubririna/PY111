from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    len_ = len(container)
    if len_ <= 1:
        return container
    for i in range(len_ - 1):
        flag = False
        for j in range(len_ - i - 1):
            if container[j + 1] < container[j]:
                container[j + 1], container[j] = container[j], container[j + 1]
                flag = True
        if not flag:
            return container

    # TODO реализовать алгоритм сортировки пузырьком
