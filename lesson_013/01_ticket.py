# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
import argparse

from PIL import Image, ImageDraw, ImageFont


def make_ticket_v1(fio="Иванов Иван Иванович", from_="Уфа", to="Екатеринбург", date="22.07.2021"):
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


def main_v1():
    make_ticket_v1(fio="Иванов Иван Иванович", from_="Уфа9", to="Екатеринбург", date="22.07.2021")


def make_ticket(fio="Иванов И.И.", from_="Уфа", to="Екатеринбург", date="22.07.2021", path=None):
    root_path = os.path.dirname(__file__)
    root_path = os.path.normpath(root_path)
    path_template = os.path.join(root_path, "images/ticket_template.png")
    path_template = os.path.normpath(path_template)
    image = Image.open(path_template)

    draw = ImageDraw.Draw(image)
    font_path = os.path.join(root_path, "python_snippets/fonts/ofont.ru_Quicksand.ttf")
    font_path = os.path.normpath(font_path)
    print(font_path)
    font = ImageFont.truetype(font_path, size=14)
    color = ('#1C0606')
    draw.text((48, 120), fio, font=font, fill=color)
    draw.text((48, 190), from_, font=font, fill=color)
    draw.text((48, 256), to, font=font, fill=color)
    draw.text((290, 258), date, font=font, fill=color)
    file_name = fio + ' ' + from_ + ' ' + to + ' ' + date + '.png'
    if path is None:
        file = os.path.join(os.path.dirname(__file__), file_name)
    else:
        path = os.path.normpath(path)
        file = os.path.join(path, file_name)
    image.save(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ping script")

    parser.add_argument("-a", dest="fio", required=True)
    parser.add_argument("-b", dest="from_", required=True)
    parser.add_argument("-c", dest="to", required=True)
    parser.add_argument("-d", dest="date", required=True)
    parser.add_argument("-e", dest="path")

    args = parser.parse_args()

    make_ticket(args.fio, args.from_, args.to, args.date, args.path)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
