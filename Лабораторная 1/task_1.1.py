import doctest
from abc import ABC, abstractmethod


# noinspection PyUnusedLocal
class Brush(ABC):
    @abstractmethod
    def __init__(self, long: float, material: str):
        """
        Создание объекта "Кисть".

        :param long: Размер кисти.
        :param material: Материал, из которого сделана кисть.
        """
        ...

    @abstractmethod
    def dip_into_paint(self, color: str) -> None:
        """
        Погружение кисти в краску.

        :param color: Цвет краски.
        """
        ...

    @abstractmethod
    def paint(self, canvas: "Canvas") -> None:
        """
        Рисование на холсте.

        :param canvas: Холст, на котором рисуется.
        """
        ...


# noinspection PyUnusedLocal
class Gouache(ABC):
    @abstractmethod
    def __init__(self, color: str, tube_size: float):
        """
        Создание объекта "Гуашь".

        :param color: Цвет гуаши.
        :param tube_size: Размер тюбика гуаши.
        """
        ...

    @abstractmethod
    def squeeze_out(self, amount: float) -> None:
        """
        Выдавливание гуаши из тюбика.

        :param amount: Количество выдавливаемой гуаши.
        """
        ...

    @abstractmethod
    def mix_color(self, other_color: str) -> str:
        """
        Смешивание цветов гуаши.

        :param other_color: Другой цвет гуаши.

        :return: Полученный цвет после смешивания.
        """
        ...


# noinspection PyUnusedLocal
class Canvas(ABC):
    @abstractmethod
    def __init__(self, size: tuple, material: str):
        """
        Создание объекта "Холст".

        :param size: Размер холста в виде кортежа (ширина, высота).
        :param material: Материал, из которого сделан холст.
        """
        ...

    @abstractmethod
    def stretch_canvas(self) -> None:
        """
        Растягивание холста.
        """
        ...

    @abstractmethod
    def prepare_surface(self) -> None:
        """
        Подготовка поверхности холста.
        """
        ...


# noinspection PyUnusedLocal
class Painting(ABC):
    @abstractmethod
    def __init__(self, style: str, artist: str, canvas: "Canvas"):
        """
        Создание объекта "Картина".

        :param style: Стиль картины.
        :param artist: Художник, создавший картину.
        :param canvas: Холст, на котором создана картина.
        """
        ...

    @abstractmethod
    def hang_on_wall(self) -> None:
        """
        Повесить картину на стену.
        """
        ...

    @abstractmethod
    def describe_painting(self) -> str:
        """
        Получить описание картины.

        :return: Описание картины.
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
