from libros import Libro

class Biblioteca:
    def __init__(self, name) -> None:
        self.name = name
        self.libros: list[Libro] = []
        self.usuarios: list = []

    def libros_disponibles(self):
        return [libro.titulo for libro in self.libros if libro.disponible]
