# qa_python

Реализованные тесты:

1. test_add_new_book_title_less_than40_successfull (параметризованный)
    Проверка правильности добавления книги при длине названия не больше 40 символов

2. test_add_new_book_title_greater_than40_unsuccessfull (параметризованный)
    Проверка корректности работы (книга не добавляется) при добавлении книги с названием длинее 40 символов

3. test_add_new_book_twice_unsuccessfull 
    Проверка корректности работы при добавлении одной и той же книги дважды (должна добавиться только один раз)

4. test_set_book_genre_from_list_successfull (параметризованный)
    Проверка правильности назначения жанра книге (жанр из списка)

5. test_get_book_genre_from_list_successfull (параметризованный)
    Проверка правильности получения жанра книни (жанр из списка)

6. test_set_book_genre_not_from_list_unsuccessfull (параметризованный)
    Проверка корректности работы при назначении жанра не из списка (в поле жанр ожидается пустая строка)

7. test_get_book_genre_not_from_list_empty_string
    Проверка корректности работы при получении жанра у книги, не добавленной в список (ожидается что результат None)

8. test_get_books_with_specific_genre_from_list_successfull
    Проверка правильности работы при запросе списка книг конкретных жанров из списка
    
9. test_get_books_with_specific_genre_not_from_list_empty_list
    Проверка корректности работы при запросе списка книг конкретного жанра, если в списке нет книг с таким жанром (ожидаетсяя пустой список)
    
10. test_get_books_for_children_not_from_age_genre_rating_successfull
    Проверка правильности запроса книг для детей (ожидается что в списке не будет книг с возрастным ограничением)
    
11. test_get_books_for_children_from_age_genre_rating_empty_list
    Проверка корректности работы при запросе книг для детей, при этом в списке нет таких книг (ожидается пустой список)

12. test_add_book_in_favorites_from_books_genre_list_successfull (параметризованный)
    Проверка правильности добавления книги в избранное

13. test_add_book_in_favorites_not_from_books_genre_list_empty_list
    Проверка корректности работы при добавлении книги в избранное, которой нет в списке книг (ожидается, что список избранных книг пустой)

14. test_add_book_in_favorites_from_books_genre_list_twice_len_favorites_1
    Проверка корректности добавления одной и той же книги дважды в список избранных (ожидается, что в список книга будет добавлена один раз)

15. test_delete_book_from_favorites_book_in_favorites_list_successfull
    Проверка правильности удаления книги из списка избранных

16. test_delete_book_from_favorites_book_not_in_favorites_list_unsuccessfull
    Проверка корректности работы при удалении книги из списка избранных, которой нет в этом списке