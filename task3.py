# 3. Рефакторинг.
# Дано: неоптимальный код.
#
# Задание: оптимизировать следующий код.
#
# sentences = ['капитан джек воробей',
#              'капитан дальнего плавания',
#              'ваша лодка готова, капитан']
#
# cap_count = 0
# for sentence in sentences:
#     cap_count += sentence.count('капитан')
#
# print(cap_count)


sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан',
             ]

count_of_captains = sum(_.count('капитан') for _ in sentences)

print(count_of_captains)

