# 5. Ленивая функция.
# Дано: цело число n.
#
# Задание: написать функцию-генератор, которая будет "лениво" возвращать значения от 0 до n, определенные следующими правилами.
#
# Если
# x == 0 -> -10
# x % 3 -> 45
# x % 5 -> (x / 5) + 93
#
# Иначе
# -> x / 2
#
# Пример:
#  n = 3, результат: list(f(n)) == [-10, 45, 45, 93.6]
#  n = 7, результат: list(f(n)) == [-10, 45, 45, 93.6, 45, 45, 94.2, 45]


def custom_generator(n):
    for _ in range(n+1):
        if _ == 0:
            yield -10
        elif _ % 3:
            yield 45
        elif _ % 5:
            yield (_ / 5) + 93
        else:
            yield _ / 2


n = 3
print(list(custom_generator(n)))
