class Book:
    def __init__(self, book):
        self.book = book

    def display(self):
        print('Книга:', self.book)

book_1 = Book('Мастер и Маргарита')
book_2 = Book('Мёртвые души')
book_3 = Book('Собачье сердце')

book_1.display()
book_2.display()
book_3.display()

print('-------------------------')

class Author:
    def __init__(self, book, author):
        self.book = book
        self.author = author

    def display(self):
        print('Книга:', self.book + ' | Автор: ' + self.author)

book_1 = Author('Мастер и Маргарита', 'Михаил Булгаков')
book_2 = Author('Мёртвые души', 'Николай Гоголь')
book_3 = Author('Собачье сердце', 'Михаил Булгаков')

book_1.display()
book_2.display()
book_3.display()
