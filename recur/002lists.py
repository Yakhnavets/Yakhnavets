#2. Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
#Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34
num = [1, 2, [2, 4, [[7, 8], 4, 6]]]
def sum_all(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum_all(element)
        else:
            total = total + element
    return total
print(sum_all(num))