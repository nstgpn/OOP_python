class Book:
    """ Базовый класс для всех книг. """

    def __init__(self, name: str, author: str):
        # Инициализация атрибутов книги
        self._name = name
        self._author = author

    @property
    def name(self):
        """ Геттер для атрибута name. """
        return self._name

    @property
    def author(self):
        """ Геттер для атрибута author. """
        return self._author

    def __str__(self):
        """ Строковое представление книги (для вывода на экран). """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """ Репрезентация объекта (для отладки). """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для бумажных книг, наследующий от Book. """

    def __init__(self, name: str, author: str, pages: int):
        # Вызов конструктора родительского класса
        super().__init__(name, author)
        self.pages = pages  # Инициализация количества страниц

    @property
    def pages(self):
        """ Геттер для атрибута pages. """
        return self._pages

    @pages.setter
    def pages(self, value):
        """ Сеттер для атрибута pages с проверкой корректности. """
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value  # Присваивание значения если проверка прошла успешно

    def __str__(self):
        """ Строковое представление бумажной книги. """
        return f"Бумажная книга '{self.name}'. Автор {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    """ Класс для аудиокниг, наследующий от Book. """

    def __init__(self, name: str, author: str, duration: float):
        # Вызов конструктора родительского класса
        super().__init__(name, author)
        self.duration = duration  # Инициализация продолжительности

    @property
    def duration(self):
        """ Геттер для атрибута duration. """
        return self._duration

    @duration.setter
    def duration(self, value):
        """ Сеттер для атрибута duration с проверкой корректности. """
        if not isinstance(value, float):
            raise ValueError("Продолжительность книги должна быть числом с плавающей запятой.")
        if value <= 0:
            raise ValueError("Продолжительность книги должна быть положительной.")
        self._duration = value  # Присваивание значения если проверка прошла успешно

    def __str__(self):
        """ Строковое представление аудиокниги. """
        return f"Аудиокнига '{self.name}'. Автор {self.author}. Продолжительность: {self.duration} ч."
