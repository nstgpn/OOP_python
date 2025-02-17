class Employee:
    """
    Базовый класс для сотрудников компании.

    Атрибуты:
        name (str): Имя сотрудника.
        age (int): Возраст сотрудника.
        _salary (float): Зарплата сотрудника (защищённый атрибут).
    """

    def __init__(self, name: str, age: int, salary: float) -> None:
        """
        Инициализация объекта сотрудника.

        Args:
            name (str): Имя сотрудника.
            age (int): Возраст сотрудника.
            salary (float): Зарплата сотрудника.
        """
        self.name = name
        self.age = age
        self._salary = salary  # Защищённый атрибут, чтобы не был доступен напрямую

    def work(self) -> str:
        """
        Метод, описывающий работу сотрудника.

        Returns:
            str: Сообщение о работе.
        """
        return f"{self.name} выполняет свои обязанности."

    def get_salary(self) -> float:
        """
        Возвращает зарплату сотрудника.

        Returns:
            float: Зарплата.
        """
        return self._salary

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Описание сотрудника.
        """
        return f"{self.name}, {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.

        Returns:
            str: Репрезентация объекта.
        """
        return f"Employee(name={self.name}, age={self.age}, salary={self._salary})"


class Manager(Employee):
    """
    Класс, представляющий менеджера, наследуется от Employee.

    Атрибуты:
        team_size (int): Количество людей в подчинении.
    """

    def __init__(self, name: str, age: int, salary: float, team_size: int) -> None:
        """
        Инициализация объекта менеджера.

        Args:
            name (str): Имя менеджера.
            age (int): Возраст менеджера.
            salary (float): Зарплата менеджера.
            team_size (int): Размер команды.
        """
        super().__init__(name, age, salary)
        self.team_size = team_size

    def work(self) -> str:
        """
        Переопределённый метод работы менеджера.

        Returns:
            str: Сообщение о работе.
        """
        return f"{self.name} управляет командой из {self.team_size} человек."

    def conduct_meeting(self) -> str:
        """
        Метод для проведения собрания.

        Returns:
            str: Сообщение о собрании.
        """
        return f"{self.name} проводит собрание с командой."

    def __repr__(self) -> str:
        """
        Репрезентация объекта для отладки.

        Returns:
            str: Репрезентация объекта.
        """
        return f"Manager(name={self.name}, age={self.age}, salary={self._salary}, team_size={self.team_size})"


class Developer(Employee):
    """
    Класс, представляющий разработчика, наследуется от Employee.

    Атрибуты:
        programming_language (str): Основной язык программирования разработчика.
    """

    def __init__(self, name: str, age: int, salary: float, programming_language: str) -> None:
        """
        Инициализация объекта разработчика.

        Args:
            name (str): Имя разработчика.
            age (int): Возраст разработчика.
            salary (float): Зарплата разработчика.
            programming_language (str): Основной язык программирования.
        """
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def work(self) -> str:
        """
        Переопределённый метод работы разработчика.

        Returns:
            str: Сообщение о работе.
        """
        return f"{self.name} пишет код на {self.programming_language}."

    def debug_code(self) -> str:
        """
        Метод для отладки кода.

        Returns:
            str: Сообщение о процессе отладки.
        """
        return f"{self.name} исправляет баги в коде."

    def __repr__(self) -> str:
        """
        Репрезентация объекта для отладки.

        Returns:
            str: Репрезентация объекта.
        """
        return f"Developer(name={self.name}, age={self.age}, salary={self._salary}, programming_language={self.programming_language})"


if __name__ == "__main__":
    manager = Manager("Алексей", 35, 150000, team_size=10)
    developer = Developer("Иван", 28, 120000, programming_language="Python")

    print(manager)  # Выводит: Алексей, 35 лет
    print(developer)  # Выводит: Иван, 28 лет

    print(manager.work())  # Выводит: Алексей управляет командой из 10 человек.
    print(developer.work())  # Выводит: Иван пишет код на Python.

    print(manager.conduct_meeting())  # Выводит: Алексей проводит собрание с командой.
    print(developer.debug_code())  # Выводит: Иван исправляет баги в коде.

    print(manager.get_salary())  # Выводит: 150000
    print(developer.get_salary())  # Выводит: 120000

    print(repr(manager))  # Выводит: Manager(name=Алексей, age=35, salary=150000, team_size=10)
    print(repr(developer))  # Выводит: Developer(name=Иван, age=28, salary=120000, programming_language=Python)
