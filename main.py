class Book:

    def __init__(self, title, author, popular, isbn, disponible=True):
        self.title = title
        self.author = author
        self.popular = popular
        self.isbn = isbn
        self.disponible = disponible
        self.__historial_prestamos = 0

    def __str__(self):
        return f"{self.title} por {self.author}, disponible: {self.disponible}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__historial_prestamos += 1
            return f"{self.title}: prestado exitosamente. Total préstamos: {self.__historial_prestamos}"
        return f"{self.title} no está disponible"

    def devolver(self):
        self.disponible = True
        return f"{self.title}, devuelto y disponible nuevamente"

    def is_popular(self):
        return self.historial_prestamos > 5

    def get__historial_prestamos(self):
        return self.__historial_prestamos

    def set_historial_prestamos(self, historial_prestamos):
        self.__historial_prestamos = historial_prestamos

my_book = Book("100 años de soledad", " Gabriel Garcia Marquez", "very popular", "1212121212", True)
another_book = Book("El principito", "Saint-Exupéry", "is popular", "141414141414", True)

my_book.set_historial_prestamos(10)
print(my_book.get__historial_prestamos())

# print(my_book.prestar())
# print(my_book.prestar())
# print(my_book.devolver())

catalogo = (my_book, another_book)

for book in catalogo:
    print(book)

