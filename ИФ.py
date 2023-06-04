def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом
    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if n < 0:
        raise ValueError("Факториал считается от положительных чисел")
    val = 1
    for i in range(1, n + 1):
        val *= i
    return val
