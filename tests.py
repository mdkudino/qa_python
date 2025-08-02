import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.mark.parametrize("name", ['Чебурашка', 'Гордость и предубеждение и зомби', 'Гордость и предубеждение и зомби .......'])
    def test_add_new_book_title_less_than40_successfull(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("name", ['Гордость и предубеждение и зомби и пираты карибского моря', 
                                      'Ехала машина полный бак бензина ехала ехала и в гараж заехала',
                                      'По поля по полям синий трактор едет к нам'])
    def test_add_new_book_title_greater_than40_unsuccessfull(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_twice_unsuccessfull(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')

        assert len(collector.get_books_genre()) == 1
    
    @pytest.mark.parametrize('name,genre', [['Гордость и предубеждение', 'Детективы'], ['Преступление и наказание', 'Ужасы']])
    def test_set_book_genre_from_list_successfull(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_books_genre()) == 1
        assert collector.get_book_genre(name) == genre
    
    @pytest.mark.parametrize('name,genre', [['Гордость и предубеждение', 'Драма'], ['Игра в кальмара', 'Дорама']])
    def test_set_book_genre_not_from_list_unsuccessfull(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_books_genre()) == 1
        assert collector.get_book_genre(name) == ''

    def test_get_book_genre_not_from_list_empty_string(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        wrong_name = "Преступление и наказание"

        assert len(collector.get_books_genre()) == 1
        assert collector.get_book_genre(wrong_name) is None

    def test_get_books_with_specific_genre_from_list_successfull(self):
        collector = BooksCollector()
        name1 = 'Гордость и предубеждение'
        genre1 = 'Детективы'

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        name2 = 'Преступление и наказание'
        genre2 = 'Детективы'

        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre2)

        name3 = 'Один дома'
        genre3 = 'Комедии'

        collector.add_new_book(name3)
        collector.set_book_genre(name3, genre3)        

        assert len(collector.get_books_genre()) == 3
        assert len(collector.get_books_with_specific_genre(genre2)) == 2
        assert len(collector.get_books_with_specific_genre(genre3)) == 1

    
    def test_get_books_with_specific_genre_not_from_list_empty_list(self):
        collector = BooksCollector()
        name1 = 'Гордость и предубеждение'
        genre1 = 'Детективы'

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        name2 = 'Преступление и наказание'
        genre2 = 'Детективы'

        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre2)

        name3 = 'Один дома'
        genre3 = 'Комедии'

        collector.add_new_book(name3)
        collector.set_book_genre(name3, genre3)        

        assert len(collector.get_books_genre()) == 3
        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 0
    
    def test_get_books_for_children_not_from_age_genre_rating_successfull(self):
        collector = BooksCollector()
        name1 = 'Алёша Попович'
        genre1 = 'Комедии'

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        name2 = 'Преступление и наказание'
        genre2 = 'Детективы'

        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre2)

        name3 = 'Простоквашино'
        genre3 = 'Мультфильмы'

        collector.add_new_book(name3)
        collector.set_book_genre(name3, genre3)        

        assert len(collector.get_books_genre()) == 3
        assert len(collector.get_books_for_children()) == 2
        assert 'Преступление и наказание' not in collector.get_books_for_children()

    def test_get_books_for_children_from_age_genre_rating_empty_list(self):
        collector = BooksCollector()
        name1 = 'Гордость и предубеждение'
        genre1 = 'Детективы'

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        name2 = 'Преступление и наказание'
        genre2 = 'Детективы'

        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre2)

        assert len(collector.get_books_genre()) == 2
        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_from_books_genre_list_successfull(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_not_from_books_genre_list_empty_list(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        name2 = 'Преступление и наказание'
        collector.add_book_in_favorites(name2)

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_from_books_genre_list_twice_len_favorites_1(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_in_favorites_list_successfull(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        name2 = 'Простоквашино'
        genre2 = 'Мультфильмы'

        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre2)
        collector.add_book_in_favorites(name2)        

        assert len(collector.get_list_of_favorites_books()) == 2
        collector.delete_book_from_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_not_in_favorites_list_unsuccessfull(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        name2 = 'Простоквашино'
        genre2 = 'Мультфильмы'

        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre2)   

        assert len(collector.get_list_of_favorites_books()) == 1
        collector.delete_book_from_favorites(name2)
        assert len(collector.get_list_of_favorites_books()) == 1
