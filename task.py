
class Shoes:
    """
    Базовый класс для всей обувь

    :param brand(str): наименование бренда
    :param model(str): название обуви
    :param article(int): артикул

    Инкапсуляция нужна, чтобы базовые настройки класса нельзя было поменять из вне

    """

    def __init__(self, brand: str, model: str, article: int):
        self._brand = brand
        self._model = model
        self._article = article

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def article(self) -> int:
        return self._article

    def __str__(self) -> str:
        return f"Brand: {self.brand}, model: {self.model}, article: {self.article}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, article={self.article!r})"


class Sneakers(Shoes):
    """
    Дочерний класс для кроссовок

    :param brand(str): наименование бренда
    :param model(str): название обуви
    :param article(int): артикул
    :param material(str): материал верха кроссовок

    """

    def __init__(self, brand: str, model: str, article: int, material: str):
        super().__init__(brand, model, article)
        self.material = material

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Материал должен быть тип str")
        self._material = value

    def waterproof(self) -> bool:
        """
        Метод выводит True или False на вопрос: "Непромокаемая ли обувь?" и по артиклу база ищется
        :return: bool
        """
        return True or False

    def season(self) -> str:
        """
        Перегрузка метода сезонности обуви
        Различия от базового, что в базовом - все сезона, а в кроссовках - лето
        :return: строка сезонности кроссовок
        """
        return "Лето"

    def __str__(self) -> str:
        return f"Brand: {self.brand}, model: {self.model}, article: {self.article}, material: {self.material}"
