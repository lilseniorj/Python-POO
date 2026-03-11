from biblioteca import Biblioteca
from exceptions import UsuarioNoEncontradoError
from libros import LibroFisico
from usuarios import Estudiante, Profesor

biblioteca = Biblioteca("Platzi Biblioteca")

estudiante = Estudiante("Jesus", "123456", "Sistema")
estudiante_1 = Estudiante("David", "1423456", "Salud")
profesor = Profesor("Luis", "4123123")

mi_libro = LibroFisico(
    "100 Años de Soledad",
    "Gabriel Garcia Marquez",
    "9781644734728",
)
otro_libro = LibroFisico(
    "El Principito",
    "Saint-Exupéry",
    "9781644731234728",
)

biblioteca.usuarios = [estudiante, estudiante_1, profesor]
biblioteca.libros = [mi_libro, otro_libro]

print("Bienvenido a lil Biblioteca")

print("Libros disponibles: ")
for titulo in biblioteca.libros_disponibles():
    print(f" - {titulo}")
print()
123456

id = input("Digite el numero de cedula: ")
try:
    usuario = biblioteca.buscar_usuario(id)
except UsuarioNoEncontradoError:
    print("El usuario que buscas no existe.")

print(usuario.name, usuario.id)
