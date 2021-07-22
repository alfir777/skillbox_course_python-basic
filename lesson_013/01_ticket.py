# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os

from PIL import Image, ImageDraw, ImageFont


def make_ticket(fio="Иванов Иван Иванович", from_="Уфа", to="Екатеринбург", date="22.07.2021"):
    path = "images//ticket_template.png"
    path = os.path.normpath(path)
    image = Image.open(path)

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("python_snippets//fonts//ofont.ru_Quicksand.ttf", size=14)
    color = ('#1C0606')
    draw.text((48, 120), fio, font=font, fill=color)
    draw.text((48, 190), from_, font=font, fill=color)
    draw.text((48, 256), to, font=font, fill=color)
    draw.text((290, 258), date, font=font, fill=color)
    file_name = fio + ' ' + from_ + ' ' + to + ' ' + date + '.png'
    image.save(file_name)


if __name__ == '__main__':
    make_ticket(fio="Иванов Иван Иванович", from_="Уфа9", to="Екатеринбург", date="22.07.2021")

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
