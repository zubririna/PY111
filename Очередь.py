"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди слева, конец - справа
        """
        self.queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди
        :param elem: Элемент, который должен быть добавлен
        Сложность 0(N)
        """

        self.queue.append(elem)    # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.
        :raise: IndexError - Ошибка, если очередь пуста
        :return: Извлеченный с начала очереди элемент.
        Сложность 0(N)
        """

        if not self.queue:                          # TODO реализовать метод dequeue
            raise IndexError("Очередь пуста")
        output = self.queue[0]
        del self.queue[0]
        return output

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.
        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)
        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди
        :return: Значение просмотренного элемента
        Сложность 0(N)
        """

        if not isinstance(ind, int):                    # TODO реализовать метод peek
            raise TypeError("Индекс не целый")
        if not 0 <= ind <= len(self.queue):
            raise IndexError("Индекс вне границ")
        return self.queue[ind]

    def clear(self) -> None:
        """ Очистка очереди.
        Сложность 0(N)
        """

        self.queue.clear()          # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди.
        Сложность 0(N)
        """

        count = 0                     # TODO реализовать метод __len__
        if self.queue:
            for val in self.queue:
                count += 1
        return count
