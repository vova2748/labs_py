from task_1 import *

if __name__ == "__main__":

    rose = Flowers('роза', 50)
    supra_A80 = Car('Toyota', 1996, 3_999_999)
    dark_side = HookahTobacco('DarkSide', 'Черника и сирень', 305)

    try:
        rose.remove_count_flowers(70)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        supra_A80.production_year_update('1995')
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        dark_side.total_amount(-5)
    except ValueError:
        print('Ошибка: неправильные данные')
