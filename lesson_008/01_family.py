# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint, choice


# ------------------- Часть первая ------------------------------
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    food_rate = 0
    cat_food_rate = 0
    money_rate = 0

    def __init__(self):
        self.food = 50
        self.money = 100
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'В доме в холодильнике еды осталось {}, еды кота осталось {}, денег в тумбочке осталось {}'.format(
            self.food, self.cat_food, self.money)


def go_to_the_house_cat(cat, house):
    cat.house = house
    cprint('{} въехал в дом'.format(cat.name), color='cyan')


class HuMen:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = None
        self.life = True

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def go_to_the_house(self, house):
        if type(self) == Husband:
            cprint('{} въехал в дом'.format(self.name), color='cyan')
        else:
            cprint('{} въехала в дом'.format(self.name), color='cyan')
        self.house = house
        self.fullness -= 10

    def eat(self):
        if self.house.food >= 10:
            if type(self) == Husband:
                cprint('{} поел'.format(self.name), color='yellow')
            else:
                cprint('{} поела'.format(self.name), color='yellow')
            fullness = randint(10, 30)
            self.fullness += fullness
            self.house.food -= fullness
            self.house.food_rate += fullness
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def pet_the_cat(self):
        if type(self) == Husband:
            cprint('{} погладил кота'.format(self.name), color='yellow')
        else:
            cprint('{} погладила кота'.format(self.name), color='yellow')
        self.happy += 5


class Husband(HuMen):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            self.life = False
            return
        if self.happy < 10:
            cprint('{} умер от депресии...'.format(self.name), color='red')
            self.life = False
            return
        dice = randint(1, 2)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.gaming()
        self.house.dirt += 5
        if self.house.dirt > 90:
            self.happy -= 10

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += self.salary
        self.house.money_rate += self.salary
        self.fullness -= 10

    def gaming(self):
        cprint('{} играл  в WoT целый день'.format(self.name), color='green')
        self.happy += 20
        self.fullness -= 10


class Wife(HuMen):
    coat_rate = 0

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умерла...'.format(self.name), color='red')
            self.life = False
            return
        if self.happy < 10:
            cprint('{} умерла от депресии...'.format(self.name), color='red')
            self.life = False
            return
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 50:
            self.shopping()
        elif self.house.cat_food < 50:
            self.shopping_cat_food()
        elif 90 < self.house.dirt < 100:
            self.happy -= 10
        elif self.house.dirt > 100:
            self.clean_house()
        else:
            self.buy_fur_coat()

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
        self.fullness -= 10

    def shopping_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
        self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money >= 350:
            cprint('{} купила шубу'.format(self.name), color='magenta')
            self.house.money -= 350
            self.happy += 60
            Wife.coat_rate += 1
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
        self.fullness -= 10

    def clean_house(self):
        self.house.dirt -= 100
        cprint('{} убралась в доме!'.format(self.name), color='red')
        self.fullness -= 10


def main1():
    if __name__ == "__main__":
        home1 = House()
        serge1 = Husband(name='Сережа', salary=150)
        serge1.go_to_the_house(house=home1)
        masha1 = Wife(name='Маша')
        masha1.go_to_the_house(house=home1)

        for day in range(365):
            cprint('================== День {} =================='.format(day), color='red')
            serge1.act()
            masha1.act()
            cprint(serge1, color='cyan')
            cprint(masha1, color='cyan')
            cprint(home1, color='cyan')
        cprint('-' * 70, color='red')
        cprint('ИТОГО: заработано денег {}, сьедено еды {}, куплено шуб {}'.format(
            home1.money_rate, home1.food_rate, masha1.coat_rate), color='red')
        cprint('-' * 70, color='red')

# ------------------- Часть вторая ------------------------------
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 30
        self.life = True

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умерла...'.format(self.name), color='red')
            self.life = False
            return
        dice = randint(1, 2)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.soil()

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            fullness = randint(1, 10)
            self.fullness += fullness * 2
            self.house.cat_food -= fullness
            self.house.cat_food_rate += fullness
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спит целый день'.format(self.name), color='green')
        self.fullness -= 10

    def soil(self):
        self.house.dirt += 5
        cprint('{} дерет обои'.format(self.name), color='blue')
        self.fullness -= 10


def main2():
    if __name__ == "__main__":
        home2 = House()
        serge2 = Husband(name='Сережа', salary=150)
        serge2.go_to_the_house(house=home2)
        masha2 = Wife(name='Маша')
        masha2.go_to_the_house(house=home2)
        bars2 = Cat('Барсик')
        go_to_the_house_cat(cat=bars2, house=home2)

        for day in range(365):
            cprint('================== День {} =================='.format(day), color='red')
            serge2.act()
            masha2.act()
            bars2.act()
            cprint(serge2, color='cyan')
            cprint(masha2, color='cyan')
            cprint(bars2, color='cyan')
            cprint(home2, color='cyan')
        cprint('-' * 70, color='red')
        cprint('ИТОГО: заработано денег {}, сьедено еды {}, куплено шуб {}'.format(
            home2.money_rate, home2.food_rate, masha2.coat_rate), color='red')
        cprint('-' * 70, color='red')


# ------------------- Часть вторая (бис)  ------------------------------
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(HuMen):

    def __init__(self, name):
        super().__init__(name)
        self.happy = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            self.life = False
            return
        if self.fullness < 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            fullness = randint(1, 10)
            self.fullness += fullness
            self.house.food -= fullness
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спит целый день'.format(self.name), color='green')
        self.fullness -= 10


def main2_master():
    if __name__ == "__main__":
        home22 = House()
        serge22 = Husband(name='Сережа', salary=150)
        serge22.go_to_the_house(house=home22)
        masha22 = Wife(name='Маша')
        masha22.go_to_the_house(house=home22)
        baby22 = Child(name='Ребенок')
        baby22.go_to_the_house(house=home22)
        bars22 = Cat('Мурзик')
        go_to_the_house_cat(cat=bars22, house=home22)

        for day in range(365):
            cprint('================== День {} =================='.format(day), color='red')
            serge22.act()
            masha22.act()
            baby22.act()
            bars22.act()
            cprint(serge22, color='cyan')
            cprint(masha22, color='cyan')
            cprint(baby22, color='cyan')
            cprint(bars22, color='cyan')
            cprint(home22, color='cyan')
        cprint('-' * 70, color='red')
        cprint('ИТОГО: заработано денег {}, сьедено еды {}, куплено шуб {}'.format(
            home22.money_rate, home22.food_rate, masha22.coat_rate), color='red')
        cprint('-' * 70, color='red')


# ------------------- Часть третья ------------------------------
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


def emulate_life(max_cats=3, salary=50, money_incidents=5, food_incidents=5):
    home = House()
    serge = Husband(name='Сережа', salary=salary)
    serge.go_to_the_house(house=home)
    masha = Wife(name='Маша')
    masha.go_to_the_house(house=home)
    baby = Child(name='Ребенок')
    baby.go_to_the_house(house=home)
    cat_names = ['Мурзик', 'Барсик', 'Борис',
                 'Альфа', 'Бета', 'Гамма', 'Эпсилон',
                 'Ньютон', 'Эйнштейнн', 'Паскаль', ]
    cats = [Cat(name=choice(cat_names)) for _ in range(max_cats)]
    for cat in cats:
        go_to_the_house_cat(cat=cat, house=home)

    for day in range(365):
        cprint('================== День {} =================='.format(day), color='red')
        serge.act()
        masha.act()
        baby.act()
        for cat in cats:
            cat.act()
        if not serge.life or not masha.life or not baby.life:
            cprint('Эксперимент провален')
            break
        for cat in cats:
            cat.act()
            if not cat.life:
                cprint('Эксперимент провален')
                break
        cprint(serge, color='cyan')
        cprint(masha, color='cyan')
        cprint(baby, color='cyan')
        for cat in cats:
            cprint(cat, color='cyan')
        if food_incidents > 0:
            fail_day_food_incidents = randint(1, 30)
            if fail_day_food_incidents == 4 and food_incidents > 0:
                home.food //= 2
                food_incidents -= 1
                cprint('Пропадает половина еды из холодильника (коты?)', color='red')
        if money_incidents > 0:
            fail_money_incidents = randint(1, 30)
            if fail_money_incidents == 13 and money_incidents > 0:
                home.money //= 2
                money_incidents -= 1
                cprint('Пропадает половина денег из тумбочки (муж? жена? коты?!?!)', color='red')
        cprint(home, color='cyan')
    cprint('-' * 70, color='red')
    cprint('ИТОГО: заработано денег {}, сьедено еды {}, куплено шуб {}'.format(
        home.money_rate, home.food_rate, masha.coat_rate), color='red')
    cprint('-' * 70, color='red')


if __name__ == '__main__':
    emulate_life(max_cats=2, salary=400, money_incidents=2, food_incidents=2)

#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
