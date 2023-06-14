"""Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
Т.е. для строк
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA
(в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку"""


from random import choice, randint
from collections import Counter

list_ = ["A", "B", "C", "D"]

list_2 = []
for n in range(randint(2, 10)):
    list_2.append("".join([choice(list_) for m in range(4)]))

print(list_2)

count, output = [], []
for i in range(len(list_2[0])):
    for j in range(len(list_2)):
        count.append(list_2[j][i])
    word = "".join(count)
    c = Counter(word)
    output.append(list(c.most_common())[0][0])
    count = []

print(f'Получилась следующая консенсус-строка: {"".join(output)}')






