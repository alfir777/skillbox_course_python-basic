# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger


def double_cheeseburger():
    my_burger.add_bun()
    my_burger.add_mayonnaise()
    my_burger.add_cucumber()
    my_burger.add_tomato()
    my_burger.add_cutlets()
    my_burger.add_cheese()
    print('Готово')

def burger():
    my_burger.add_bun()
    my_burger.add_cutlets()
    my_burger.add_mayonnaise()
    my_burger.add_cutlets()
    my_burger.add_cucumber()
    my_burger.add_cutlets()
    my_burger.add_tomato()
    my_burger.add_cutlets()
    my_burger.add_cheese()
    print('Готово')


print('Рецепт двойного чизбургера')
double_cheeseburger()
print('-' * 30)
print('Рецепт своего бургера')
burger()
