# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

snowflakes_count = 20

snowfall.create_snowflakes(snowflakes_count=snowflakes_count)

while True:
    sd.start_drawing()
    snowfall.draw_snowflakes(color=sd.background_color)
    snowfall.move_snowflakes()
    snowfall.draw_snowflakes(color=sd.COLOR_WHITE)

    down_snowflakes = snowfall.get_down_snowflakes()

    if len(down_snowflakes) > 0:
        snowfall.remove_snowflakes(num_snowflake=down_snowflakes)
        snowfall.create_snowflakes(snowflakes_count=len(down_snowflakes))

    sd.sleep(0.05)
    sd.finish_drawing()

    if sd.user_want_exit():
        break
