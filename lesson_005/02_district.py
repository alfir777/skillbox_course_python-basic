# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as central_street_room1
from district.central_street.house1 import room2 as central_street_room2
from district.soviet_street.house1 import room1 as soviet_street_room1
from district.soviet_street.house1 import room2 as soviet_street_room2

print('На Центральном районе живут:',
      ', '.join(central_street_room1.folks),
      ', '.join(central_street_room2.folks))

print('На Советском районе живут:',
      ', '.join(soviet_street_room1.folks),
      ', '.join(soviet_street_room2.folks))



