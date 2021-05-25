# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if type(other) == Air:
            return Storm().__str__()
        elif type(other) == Fire:
            return Steam().__str__()
        elif type(other) == Earth:
            return Dirt().__str__()

    def __str__(self):
        return self.name


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if type(other) == Water:
            return Storm().__str__()
        elif type(other) == Fire:
            return Lightning().__str__()
        elif type(other) == Earth:
            return Dust().__str__()

    def __str__(self):
        return self.name


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if type(other) == Water:
            return Steam().__str__()
        elif type(other) == Air:
            return Lightning().__str__()
        elif type(other) == Earth:
            return Lava().__str__()

    def __str__(self):
        return self.name


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if type(other) == Water:
            return Dirt().__str__()
        elif type(other) == Air:
            return Dust().__str__()
        elif type(other) == Fire:
            return Lava().__str__()

    def __str__(self):
        return self.name


class Storm:
    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return self.name


class Steam:
    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name


class Dirt:
    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return self.name


class Lightning:
    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return self.name


class Dust:
    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return self.name


class Lava:
    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return self.name


print(Water(), '+', Air(), '=')
print(Water(), '+', Air(), '=', Air() + Water())
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
