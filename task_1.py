class Flowers:
    def __init__(self, name: str, count: int):
        """
        Создание и подготовка к работе объекта "Цветы"

        :param name: наименование цветка
        :param count: количество цветов

        Пример:
        >>> rose = Flowers('роза', 50) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name

        if not isinstance(count, int):
            raise TypeError("Количество должно быть типа int")
        if count < 0:
            raise ValueError("Количество должно быть неотрицательным числом")
        self.count = count

    def remove_count_flowers(self, remove_count: int) -> str:
        """
        Функция обновляет количество на складе

        :param remove_count: количество цветов, которое купили
        :return: остаток на складе

        >>> rose = Flowers('роза', 50)
        >>> rose.remove_count_flowers(25)
        'Осталось 25 роза'
        """
        if not isinstance(remove_count, int):
            raise TypeError("Количество должно быть типа int")
        if remove_count > self.count:
            raise ValueError("Число превышает количество в наличии")
        self.count -= remove_count

        return f"Осталось {self.count} {self.name}"

    def add_count_flowers(self, add_count: int = 50) -> None:
        """
        Функция обновляет количество на складе

        :param add_count: количество цветов, доставленных в салон
        :return: новый остаток на складе

        >>> rose = Flowers('роза', 50)
        >>> rose.add_count_flowers()
        Количество роза теперь 100
        """
        if not isinstance(add_count, int):
            raise TypeError("Количество должно быть типа int")
        if add_count <= 0:
            raise ValueError("Число должно быть положительным")
        self.count += add_count

        print(f"Количество {self.name} теперь {self.count}")


class Car:
    def __init__(self, manufacturer: str, year: int, price: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param manufacturer: производитель автомобиля
        :param year: год производства
        :param price: цена

        >>> supra_A80 = Car('Toyota', 1996, 3_999_999)

        """
        if not isinstance(manufacturer, str):
            raise TypeError("Производитель должен быть типа str")
        self.manufacturer = manufacturer

        if not isinstance(year, int):
            raise TypeError("Год должен быть типа int")
        if year <= 0:
            raise ValueError("Год должен быть положительным числом")
        self.year = year

        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int")
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = price

    def description(self) -> str:
        """
        Функция возвращает описание автомобиля

        :return: описание автомобиля

        >>> supra_A80 = Car('Toyota', 1996, 3_999_999)
        >>> supra_A80.description()
        'Производитель: Toyota, год производства: 1996, цена: 3999999'
        """

        return f"Производитель: {self.manufacturer}, год производства: {self.year}, цена: {self.price}"

    def production_year_update(self, new_year: int = 2024) -> None:
        """
        Функция обновляет год для модели автомобиля

        :param new_year: год для обновленной модели автомобиля
        :return: обновленный год производства

        >>> supra_A80 = Car('Toyota', 1996, 3_999_999)
        >>> supra_A80.production_year_update(1999)
        Обновленный год: 1999
        """

        if not isinstance(new_year, int):
            raise TypeError("Год должен быть типа int")
        if new_year <= 0:
            raise ValueError("Год должен быть положительным числом")

        self.year = new_year
        print(f"Обновленный год: {self.year}")


class HookahTobacco:
    def __init__(self, name: str, aroma: str, price: float):
        """
        Создание и подготовка к работе объекта "Табак для кальяна"

        :param name: производитель табака
        :param aroma: вкус (ароматизатор) табака
        :param price: цена

        >>> dark_side = HookahTobacco('DarkSide', 'Черника и сирень', 305)
        """
        if not isinstance(name, str):
            raise TypeError("Производитель должен быть типа str")
        self.name = name

        if not isinstance(aroma, str):
            raise TypeError("Производитель должен быть типа str")

        self.aroma = aroma

        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int")
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = price

    def description(self) -> str:
        """
        Функция возвращает описание продукта

        :return: описание табака

        >>> dark_side = HookahTobacco('DarkSide', 'Черника и сирень', 305)
        >>> dark_side.description()
        'Производитель: DarkSide, вкус: Черника и сирень, цена: 305'
        """

        return f"Производитель: {self.name}, вкус: {self.aroma}, цена: {self.price}"

    def total_amount(self, count: int = 3) -> float:
        """
        Функция возвращает сумму покупки табака

        :param count: количество покупки табака
        :return: сумма покупки

        >>> dark_side = HookahTobacco('DarkSide', 'Черника и сирень', 305)
        >>> dark_side.total_amount(5)
        1525
        """

        if not isinstance(count, int):
            raise TypeError("Цена должна быть типа int")
        if count <= 0:
            raise ValueError("Цена должна быть положительным числом")

        total_sum = self.price * count
        return total_sum
