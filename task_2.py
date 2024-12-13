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


class Book:
    def __init__(self, id_: int, name: str, pages: int):

        if not isinstance(id_, int):
            raise TypeError("Id должно быть типа int")
        if id_ < 1:
            raise ValueError("Id должно быть неотрицательным числом")
        self.id = id_

        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество должно быть типа int")
        if pages < 1:
            raise ValueError("Количество должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        if self.books is []:
            return 1
        else:
            return 1 + len(self.books)

    def get_index_by_book_id(self, id_: int) -> str:
        if id_ <= len(self.books) and id_ != 0:
            return self.books[id_ - 1]
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
