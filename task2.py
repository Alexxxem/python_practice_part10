# 2. Длинномер.
# Дано: список строковых значений.
#
# Задание: написать функцию, которая возвращает список длин каждой строки.
#
# Пример:
#  ['Tina', 'Raj', 'Tom'], результат: [4, 3, 3]

def get_word_lengths(words):
    """
    Calculate the lengths of each word in a list of words.

    :param:
        words: the list of words
    :return:
        list: the list of word lengths
    """
    lengths = [len(_) for _ in words]
    return lengths


words = ['Tina', 'Ray', 'Tom']
print(get_word_lengths(words))
