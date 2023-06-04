def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок
    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    Сложность 0(N)
    """

    queue = []                         # TODO реализовать проверку скобочной группы
    for letter in brackets_row:  # O(N)
        if letter in ['(']:
            queue.append(letter)
        if letter in [')']:
            if not queue:
                return False
            del queue[-1]
    if queue:
        return False
    return True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
