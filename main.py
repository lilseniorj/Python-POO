class Book:

    def __init__(self, title, author, popular, isbn, disponible=True):
        self.title = title
        self.author = author
        self.popular = popular
        self.isbn = isbn
        self.disponible = disponible
        self.historial_prestamos = []

    def __str__(self):
        return f"{self.title} por {self.author}, disponible: {self.disponible}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.historial_prestamos.append(self)
            return f"{self.title}: prestado exitosamente."

    def devolver(self):
        self.disponible = True
        return f"{self.title}, devuelto y disponible nuevamente"

    def is_popular(self):
        return self.historial_prestamos.count(self) > 5

my_book = Book("100 años de soledad", " Gabriel Garcia Marquez", "very popular", "1212121212", True)
another_book = Book("El principito", "Saint-Exupéry", "is popular", "141414141414", True)

my_book.prestar()
my_book.devolver()

catalogo = (my_book, another_book)

for book in catalogo:
    print(book)

