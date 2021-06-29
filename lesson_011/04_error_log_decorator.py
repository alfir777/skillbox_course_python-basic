# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors_v1(func):
    def surrogate(*args, **kwargs):
        file = open(file='function_errors.log', mode='a', encoding='utf-8')
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as exc:
            param = []
            param.extend([arg for arg in args])
            param.extend([f'{key}={value}' for key, value in kwargs.items()])
            file.write(f'{func.__name__:<10}'
                       f'{param.__str__():<40}'
                       f'{exc.__class__.__name__:<20}'
                       f'{str(exc):<10}\n')
        file.close()
    return surrogate


def log_errors_v2(filename=None):
    def log_errors(func):
        def surrogate(*args, **kwargs):
            file = open(file=filename, mode='a', encoding='utf-8')
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as exc:
                param = []
                param.extend([arg for arg in args])
                param.extend([f'{key}={value}' for key, value in kwargs.items()])
                file.write(f'{func.__name__:<10}'
                           f'{param.__str__():<40}'
                           f'{exc.__class__.__name__:<20}'
                           f'{str(exc):<10}\n')
            file.close()
        return surrogate
    return log_errors


# Проверить работу на следующих функциях
@log_errors_v2(filename='function_errors.log')
def perky(param):
    return param / 0


@log_errors_v2(filename='function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

