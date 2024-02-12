class Animal:
    """Базовый класс Животное."""

    def __init__(self, name: str, species: str):
        """
        Инициализирует объект Животное.

        Args:
            name (str): Имя животного.
            species (str): Вид животного.
        """
        self.name = name
        self.species = species

    def make_sound(self) -> str:
        """
        Воспроизводит звук, характерный для животного.

        Returns:
            str: Звук, издаваемый животным.
        """
        pass

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.name} - {self.species}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для вывода в интерпретаторе.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, species={self.species!r})"


class Dog(Animal):
    """Дочерний класс Собака, наследующий от базового класса Животное."""

    def __init__(self, name: str, breed: str):
        """
        Инициализирует объект Собака.

        Args:
            name (str): Имя собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, species="Собака")
        self.breed = breed

    def wag_tail(self) -> str:
        """
        Имитирует виляние хвостом.

        Returns:
            str: Сообщение о вилянии хвостом.
        """
        pass

    def make_sound(self) -> str:
        """
        Воспроизводит лай собаки.

        Returns:
            str: Звук лая.
        """
        return "Гав-гав!"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для вывода в интерпретаторе.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, breed={self.breed!r})"
