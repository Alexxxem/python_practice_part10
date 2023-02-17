# 1. Градусник.
# Дано: список градусов Цельсия.
#
# Задание: написать функцию, которая преобразовывает исходный список градусов Цельсия в список градусов Фаренгейта
#
# Пример:
#
#  [39.2, 36.5, 37.3, 37.8], результат:
#  [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]


def celsius_to_fahrenheit(degrees_celsius):
    """
    Function to convert degrees Celsius to degrees Fahrenheit.
    Tf = 1.8 * Tc + 32

    :param
        degrees_celsius (list): the list of degrees Celsius

    :return:
        list: the list of degrees Fahrenheit
    """
    COEFF = 1.8
    COEFF2= 32
    degrees_fahrenheit = [COEFF * _ + COEFF2 for _ in degrees_celsius]
    return degrees_fahrenheit


degrees = [39.2, 36.5, 37.3, 37.8]
print(celsius_to_fahrenheit(degrees))
