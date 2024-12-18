import doctest
from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Булгаков", 500)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self) -> None:
        """
        Чтение книги.

        :return: None

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Булгаков", 500)
        >>> book.read()
        """
        ...

    @abstractmethod
    def bookmark(self, page: int) -> None:
        """
        Установка закладки на определенной странице.

        :param page: Страница, на которой нужно поставить закладку
        :raise ValueError: Если страница не существует в книге

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Булгаков", 500)
        >>> book.bookmark(250)
        """
        ...


class Car(ABC):
    def __init__(self, make: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param make: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        """
        if not isinstance(make, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        if year < 1886:
            raise ValueError("Год выпуска не может быть раньше 1886 года")

        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """
        Запуск двигателя автомобиля.

        :return: None

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.start_engine()
        """
        ...

    @abstractmethod
    def drive(self, speed: int) -> None:
        """
        Поездка на автомобиле.

        :param speed: Скорость автомобиля в км/ч
        :raise ValueError: Если скорость меньше 0 или превышает максимально допустимую

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.drive(80)
        """
        ...


class Refrigerator(ABC):
    def __init__(self, capacity: float, brand: str, temperature: float):
        """
        Создание и подготовка к работе объекта "Холодильник"

        :param capacity: Общий объем холодильника в литрах
        :param brand: Бренд холодильника
        :param temperature: Температура внутри холодильника в градусах Цельсия

        Примеры:
        >>> fridge = Refrigerator(300, "Samsung", 4)
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем холодильника должен быть числом (int или float)")
        if capacity <= 0:
            raise ValueError("Объем холодильника должен быть положительным числом")
        if not isinstance(brand, str):
            raise TypeError("Бренд холодильника должен быть строкой")
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")

        self.capacity = capacity
        self.brand = brand
        self.temperature = temperature

    @abstractmethod
    def set_temperature(self, temperature: float) -> None:
        """
        Установка температуры в холодильнике.

        :param temperature: Температура в градусах Цельсия
        :raise ValueError: Если температура слишком низкая или высокая для нормальной работы

        Примеры:
        >>> fridge = Refrigerator(300, "Samsung", 4)
        >>> fridge.set_temperature(3)
        """
        ...

    @abstractmethod
    def open_door(self) -> None:
        """
        Открытие двери холодильника.

        :return: None

        Примеры:
        >>> fridge = Refrigerator(300, "Samsung", 4)
        >>> fridge.open_door()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
