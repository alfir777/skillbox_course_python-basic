#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Папа', 'Мама', 'Пасынок', 'Сын']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Альфир', 170],
    ['Кристина', 165],
    ['Матвей', 140],
    ['Айдар', 100],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f'Рост {my_family[0]} - {my_family_height[0][1]} см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
growth_family = my_family_height[0][1]
growth_family += my_family_height[1][1]
growth_family += my_family_height[2][1]
growth_family += my_family_height[3][1]
print(f'Общий рост моей семьи - {growth_family} см')

# используя цикл for
growth_family = 0
for i in range(len(my_family_height)):
    growth_family += my_family_height[i][1]

print(f'Общий рост моей семьи - {growth_family} см')
