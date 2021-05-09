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

x = []
for _ in range(N):
    x.append(sd.random_number(0, 1200))
y = []
for _ in range(N):
    y.append(sd.random_number(0, 600))

while True:
    sd.start_drawing()
    for i in range(len(x)):
        if i > 0:
            point1 = sd.get_point(x[i-1], y[i-1])
            sd.snowflake(center=point1, length=50, color=sd.COLOR_WHITE)
        point = sd.get_point(x[i], y[i])
        sd.snowflake(center=point, length=50, color=sd.background_color)
        y[i] -= sd.random_number(0, 10)
        x[i] = x[i] + sd.random_number(0, 10)
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
