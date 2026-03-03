

class Book:

    def __init__(self, title, author, popular):
        self.title = title
        self.author = author
        self.popular = popular

my_book = Book("100 años de soledad", " Gabriel Garcia Marquez", "very popular")
another_book = Book("El principito", "Saint-Exupéry", "is popular")

print(f"My Book:  {my_book.title} {my_book.author}, \nPopular: {my_book.popular}")
print(f"Another Book:  {another_book.title} {another_book.author}, \nPopular: {another_book.popular}")

