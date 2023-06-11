from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # начальное поле и проход по нему (верт, гориз)
    field = [[1 for i in range(n)] for j in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            field[i][j] = field[i][j - 1] + field[i - 1][j] + field[i - 1][j - 1]
    return field

    # TODO решить задачу с помощью динамического программирования


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7



