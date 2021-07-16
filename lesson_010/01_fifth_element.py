# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    lee_loo = int(input_data[4])
    result = BRUCE_WILLIS * lee_loo
    print(f"- Lee loo Dallas! Multi-pass № {result}!")
except ValueError:
    print('Невозможно преобразовать к числу')
except IndexError:
    print('Выход за границы списка')
except Exception as exc:
    print(f'Исключительная ошибка: {exc}')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
