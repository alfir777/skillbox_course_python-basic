# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd

from painting import fractal as paint_fractal, \
    rainbow as paint_rainbow, \
    smile as paint_smile, \
    snowfall as paint_snowfall, \
    wall as paint_wall

sd.resolution = (1200, 600)

#  - кирпичный дом, в окошке - смайлик
color_home = sd.COLOR_ORANGE
coord_x = 300
coord_y = 100
start_point = sd.get_point(coord_x-3, coord_y)
paint_wall.square(start_point=start_point, angle=0, length=211, color=color_home)
paint_wall.wall(coord_x=coord_x, coord_y=coord_y, height=201)
start_point = sd.get_point(coord_x-1, coord_y+211)
paint_wall.triangle(start_point=start_point, angle=0, length=211, color=color_home)
start_point = sd.get_point(coord_x+51, coord_y+51)
sd.square(left_bottom=start_point, side=103, color=sd.background_color, width=0)
paint_wall.square(start_point=start_point, angle=0, length=101, color=color_home)
paint_smile.smile(x=coord_x+101, y=coord_y+101, size=0.5, color=sd.COLOR_CYAN)

# - справа от дома - дерево
root_point = sd.get_point(900, 30)
paint_fractal.draw_branches_v2(start_point=root_point, angle=90, length=100)

#  - справа в небе - радуга, слева - солнце (весна же!)
paint_rainbow.rainbow(size=1)
center_position = sd.get_point(100, 500)
sd.circle(center_position, radius=50, color=sd.COLOR_YELLOW, width=0)

#  - слева от дома - сугроб (предположим что это ранняя весна)
paint_snowfall.snowfall()

sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
