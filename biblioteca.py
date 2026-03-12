from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError
from libros import Libro

class Biblioteca:
    def __init__(self, name) -> None:
        self.name = name
        self.libros: list[Libro] = []
        self.usuarios: list = []

    def libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        raise UsuarioNoEncontradoError(f"El usuario con la cedula {id} no fue encontrado")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                return libro
        raise LibroNoDisponibleError(f"El libro: {titulo}, no esta disponible o no existe")

    @staticmethod
    def validar_isbn(isbn):
        return len(isbn) >= 10