# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class CheckRegistration:

    def __init__(self, incoming_files, registrations_goods, registrations_error):
        self.incoming_file = incoming_files
        self.registrations_good = registrations_goods
        self.registrations_bad = registrations_error

    def open_file(self):
        self.incoming_file = open(self.incoming_file, 'r', encoding='utf8')
        self.registrations_good = open(self.registrations_good, 'w', encoding='utf8')
        self.registrations_bad = open(self.registrations_bad, 'w', encoding='utf8')

    def close_file(self):
        self.incoming_file.close()
        self.registrations_good.close()
        self.registrations_bad.close()

    def parser(self):
        self.open_file()
        count_line = 0
        for line in self.incoming_file:
            count_line += 1
            try:
                name, email, age = line.split(' ')
                if not name and not email and not age:
                    raise ValueError
                elif not name.isalpha():
                    raise NotNameError
                elif not email.find('@') and not email.find('.'):
                    raise NotEmailError
                elif 10 < int(age) > 99:
                    raise ValueError
                else:
                    self.registrations_good.write(f'{line}')
            except ValueError:
                if not name and not email and not age:
                    self.registrations_bad.write(f'В строке {count_line} НЕ присутсвуют все три поля: {line}')
                else:
                    self.registrations_bad.write(
                        f'В строке {count_line} поле возраст НЕ является числом от 10 до 99: {line}')
            except NotNameError:
                self.registrations_bad.write(f'В строке {count_line} поле имени содержит НЕ только буквы: {line}')
            except NotEmailError:
                self.registrations_bad.write(f'В строке {count_line} поле емейл НЕ содержит @ и .(точку): {line}')
        self.close_file()


if __name__ == '__main__':
    incoming_file = 'registrations.txt'
    registrations_good = 'registrations_good.log'
    registrations_bad = 'registrations_bad.log'
    parser = CheckRegistration(incoming_files=incoming_file,
                               registrations_goods=registrations_good,
                               registrations_error=registrations_bad)
    parser.parser()
