# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 17900, 37

i = a
res = 0

while i >= 0:
    i -= b
    if i < 0:
        break
    res += 1
print('Целочисленное деление', a, 'на', b, 'дает', res)

