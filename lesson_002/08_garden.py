#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
print(garden_set)

# выведите на консоль те, которые растут и там и там
garden_meadow_set = garden_set | meadow_set
print(garden_meadow_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_meadow_set = garden_set - meadow_set
print(garden_meadow_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
garden_meadow_set = meadow_set - garden_set
print(garden_meadow_set)
