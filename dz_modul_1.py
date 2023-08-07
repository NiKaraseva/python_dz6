# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from sys import argv


__all__ = ['date_check']


def _leap_year(input_year: int):
    if (input_year % 4 == 0 and input_year % 100 != 0) or input_year % 400 == 0:
        return True
    else:
        return False


def date_check(day: int, month: int, year: int):
    list_31_days = [1, 3, 5, 7, 8, 10, 12]
    list_30_days = [4, 6, 9, 11]
    list_28_days = [2]
    # day, month, year = input_date.split('.')
    if month in list_31_days and 0 < day < 32 and 1 < year < 10000 and not _leap_year(year):
        return 'Дата существует'
    elif month in list_30_days and 0 < day < 31 and 1 < year < 10000 and not _leap_year(year):
        return 'Дата существует'
    elif month in list_28_days and 0 < day < 29 and 1 < year < 10000 and not _leap_year(year):
        return 'Дата существует'
    elif month in list_28_days or list_30_days or list_31_days and 0 < day < 30 and 1 < year < 10000 and _leap_year(year):
        return 'Дата существует и год високосный'
    else:
        return 'Дата НЕ существует'


if __name__ == "__main__":
    input_date = input('Введите дату: ')
    argv = map(int, input_date.split('.'))
    print(date_check(*argv))