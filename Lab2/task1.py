class Book:
    def __init__(self, id_, name, pages):
        # Инициализация атрибутов класса
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        # Метод для строкового представления объекта (для пользователя)
        return f'Книга "{self.name}"'

    def __repr__(self):
        # Метод для строкового представления объекта (для разработчика)
        # Возвращает строку, по которой можно создать идентичный объект
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

# База данных книг в виде списка словарей
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    # Инициализация списка объектов класса Book из базы данных
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверка работы метода __str__ (строкового представления)
    for book in list_books:
        print(book)  # Выводит: Книга "test_name_1", Книга "test_name_2"

    # Проверка работы метода __repr__ (репрезентации объекта)
    print(
        list_books)  # Выводит список: [Book(id_=1, name='test_name_1', pages=200), Book(id_=2, name='test_name_2', pages=400)]