import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture(scope='function')
    def collector(self):
        return BooksCollector()

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #1. Тест, проверяющий, что книга со слишком длинным именем не добавляется в коллектор
    def test_add_new_book_too_long_name_fail_to_add(self, collector):
        collector.add_new_book("Очень длинное имя книги не должно добавиться")
        assert len(collector.get_books_genre()) == 0

    #список названий книг с их жанром
    books_with_genres = [
        ["1",'Фантастика'],
        ["2", 'Ужасы'],
        ["3", 'Детективы'],
        ["4", 'Мультфильмы'],
        ["5", 'Комедии']
    ]
    #2. Тест, проверяющий, что можно добавить жанр. Проверяет все доступные жанры
    @pytest.mark.parametrize("name, genre", books_with_genres)
    def test_set_book_genre_genre_added(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    #3. Тест проверяет, что если добавить несуществующий в списке жанр, он не добавится
    def test_set_book_genre_genre_unknown(self, collector):
        name = "Test"
        collector.add_new_book(name)
        collector.set_book_genre(name, "Job")
        assert collector.get_book_genre(name) == ""

    #4. Тест проверяет, что функция get_books_with_specific_genre выдает книгу по заданному жанру
    #тест проверяет каждый жанр при помощи созданной ранее переменной
    @pytest.mark.parametrize("name, genre", books_with_genres)
    def test_get_books_with_specific_genre_known_book_and_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_with_specific_genre(genre)

    #список книг, у каждой два жанра
    books_and_two_genres = [
        ["1",'Фантастика', "Ужасы"],
        ["2", 'Ужасы', "Фантастика"],
        ["3", 'Детективы', "Мультфильм"],
        ["4", 'Мультфильмы', "Детективы"],
        ["5", 'Комедии', "Рабочее"]
    ]

    #5. Тест, проверяющий, что функция get_books_with_specific_genre возвращает пустой список, если
    # нет книг нужного жанра
    @pytest.mark.parametrize("name, genre, genre_wrong", books_and_two_genres)
    def test_get_books_with_specific_genre_no_book_with_genre(self, name, genre, genre_wrong, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre_wrong) == []

    # Список книг с жанрами, подходящими для детей
    books_for_children = [
        ["1", 'Фантастика'],
        ["4", 'Мультфильмы'],
        ["5", 'Комедии']
    ]

    #6. Тест, проверяющий, что функция get_books_for_children возвращает книгу, подходящую для детей,
    # для каждого из подходящих для детей жанров (переменная books_for_children)
    @pytest.mark.parametrize("name, genre", books_for_children)
    def test_get_books_for_children_when_book_is_for_children(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_for_children()

    # Список книг с жанрами, не подходящими для детей
    books_not_for_children = [
        ["2", 'Ужасы'],
        ["3", 'Детективы']
    ]

    #7. Тест, проверяющий, что функция get_books_for_children возвращает пустой список,
    # если есть только книги жанров, не подходящих для детей (переменная books_not_for_children)
    @pytest.mark.parametrize("name, genre", books_not_for_children)
    def test_get_books_for_children_empty_when_book_is_not_for_children(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == []

    #8. Тест, проверяющий, что можно добавить в список любимых книг существующую книгу
    def test_add_book_in_favorite_existing_book(self, collector):
        name = "Test"
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    #9. Тест, проверяющий, что несуществующая книга в список любимых книг не добавляется
    def test_add_book_in_favorite_not_existing_book(self, collector):
        name = "Test"
        name2 = "Test2"
        collector.add_new_book(name)
        collector.add_book_in_favorites(name2)
        assert collector.get_list_of_favorites_books() == []

    #10. Тест, проверяющий, что после удаления одной книги из двух в списке фаворитов
    # остается одна книга
    def test_delete_book_from_favorite_from_two_one_remained(self, collector):
        name = "Test"
        name2 = "Test2"
        collector.add_new_book(name)
        collector.add_new_book(name2)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name2)
        collector.delete_book_from_favorites(name2)
        assert len(collector.get_list_of_favorites_books()) == 1