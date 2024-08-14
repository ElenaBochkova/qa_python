# qa_python
<b><h1>Список тестов:</h1></b>
0. <b>test_add_new_book_add_two_books</b> - пример теста
1. <b>test_add_new_book_too_long_name_fail_to_add</b> - проверяет, что книга со слишком длинным именем не добавляется в коллектор
2. <b>test_set_book_genre_genre_added</b> - проверяет, что можно добавить жанр. Проверяет все доступные жанры. Параметризован
3. <b>test_set_book_genre_genre_unknown</b> - проверяет, что если добавить несуществующий в списке жанр, он не добавится
4. <b>test_get_books_with_specific_genre_known_book_and_genre</b> - проверяет, что функция get_books_with_specific_genre выдает книгу по заданному жанру. Тест проверяет каждый жанр при помощи созданной ранее переменной. Параметризован
5. <b>test_get_books_with_specific_genre_no_book_with_genre</b> - проверяет, что функция get_books_with_specific_genre возвращает пустой список, если нет книг нужного жанра. Параметризован
6. <b>test_get_books_for_children_when_book_is_for_children</b> - проверяет, что функция get_books_for_children возвращает книгу, подходящую для детей, для каждого из подходящих для детей жанров (переменная books_for_children). Параметризован
7. <b>test_get_books_for_children_empty_when_book_is_not_for_children</b> - проверяет, что функция get_books_for_children возвращает пустой список, если есть только книги жанров, не подходящих для детей (переменная books_not_for_children). Параметризован
8. <b>test_add_book_in_favorite_existing_book</b> - проверяет, что можно добавить в список любимых книг существующую книгу
9. <b>test_add_book_in_favorite_not_existing_book</b> - проверяет, что несуществующая книга в список любимых книг не добавляется
10. <b>test_delete_book_from_favorite_from_two_one_remained</b> - проверяет, что после удаления одной книги из двух в списке фаворитов остается одна книга