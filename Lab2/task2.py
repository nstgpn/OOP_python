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

class Library:
    def __init__(self, books=None):
        # Инициализация библиотеки с необязательным списком книг
        # Если books не передан, инициализируется пустым списком
        self.books = books if books is not None else []

    def get_next_book_id(self):
        # Метод возвращает следующий идентификатор для новой книги
        if not self.books:
            # Если список книг пуст, следующий ID будет 1
            return 1
        # Возвращаем ID последней книги + 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        # Метод возвращает индекс книги в списке по её ID
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        # Если книга не найдена, вызываем ValueError
        raise ValueError("Книги с запрашиваемым id не существует")

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

    # Проверка работы класса Library
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Выводит: 1

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Выводит: 3

    print(library_with_books.get_index_by_book_id(1))  # Выводит: 0