# 4. Возведение в степень.
# Дано: два списка одинаковой длины: чисел X и степеней Y.
#
# Задание: написать функцию, которая возвращает список [x1^y1, x2^y2, ..], где X=[x1, x2, ..], Y=[y1, y2, ..].
#
# Пример:
#  X = [2, 3, 4], Y = [10, 11, 12], результат: [1024, 177147, 16777216]


def custom_exponentiate(x, y):
    result = list(map(lambda a, b: a**b, x, y))
    return result


x = [2, 3, 4]
y = [10, 11, 12]

print(custom_exponentiate(x, y))


