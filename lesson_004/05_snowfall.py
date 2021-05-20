# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

sd.resolution = (1200, 600)

y = 550

snowflakes = {}

for i in range(N):
    snowflakes[i] = {'length': sd.random_number(5,15),
                     'x': sd.random_number(0, sd.resolution[0]),
                     'y': y,
                     'factor_a': sd.random_number(1, 10)/10,
                     'factor_b': sd.random_number(1, 10)/10,
                     'factor_c': sd.random_number(10, 120)}

while True:
    sd.start_drawing()
    for snowflakes_k, snowflakes_v in snowflakes.items():
        start_point = sd.get_point(snowflakes_v['x'], snowflakes_v['y'])
        sd.snowflake(center=start_point,
                     length=snowflakes_v['length'],
                     color=sd.background_color,
                     factor_a=snowflakes_v['factor_a'],
                     factor_b=snowflakes_v['factor_b'],
                     factor_c=snowflakes_v['factor_c'])

        snowflakes_v['x'] += sd.random_number(-5, 5)
        snowflakes_v['y'] -= snowflakes_v['length']

        next_point = sd.get_point(snowflakes_v['x'], snowflakes_v['y'])
        sd.snowflake(center=next_point,
                     length=snowflakes_v['length'],
                     color=sd.COLOR_WHITE,
                     factor_a=snowflakes_v['factor_a'],
                     factor_b=snowflakes_v['factor_b'],
                     factor_c=snowflakes_v['factor_c'])

        if snowflakes_v['y'] < 50:
            snowflakes_v['y'] = y
            snowflakes_v['x'] = sd.random_number(0, sd.resolution[0])

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
