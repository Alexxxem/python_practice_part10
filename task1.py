# 1. Градусник.
# Дано: список градусов Цельсия.
#
# Задание: написать функцию, которая преобразовывает исходный список градусов Цельсия в список градусов Фаренгейта
#
# Пример:
#
#  [39.2, 36.5, 37.3, 37.8], результат:
#  [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]


def celsius_to_fahrenheit(celsius_temperatures):
    """
    Convert a list of Celsius temperatures to Fahrenheit.
    Tf = 1.8 * Tc + 32

    :param
        celsius_temperatures (list): the list of Celsius temperatures

    :return:
        list: the list of Fahrenheit temperatures
    """
    SCALE = 1.8
    FAHRENHEIT_FREEZING_POINT = 32
    fahrenheit_temperatures = [(SCALE * _) + FAHRENHEIT_FREEZING_POINT for _ in celsius_temperatures]
    return fahrenheit_temperatures


temperatures = [39.2, 36.5, 37.3, 37.8]
print(celsius_to_fahrenheit(temperatures))
