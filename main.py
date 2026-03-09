from biblioteca import Biblioteca
from libros import LibroFisico
from usuarios import Estudiante, Profesor, SolicitanteProtocol

biblioteca = Biblioteca("Platzi Biblioteca")

estudiante = Estudiante("Jesus", "123456", "Sistema")
estudiante_1 = Estudiante("David", "1423456", "Salud")
profesor = Profesor("Luis", "4123123")

usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_1, profesor]



mi_libro = LibroFisico(
    "100 Años de Soledad",
    "Gabriel Garcia Marquez",
    "9781644734728",
    True,
)
mi_libro_no_disponible = LibroFisico(
    "No disponible",
    "Luis",
    "56789",
    True,
)
otro_libro = LibroFisico(
    "El Principito",
    "Saint-Exupéry",
    "9781644731234728",
    True,
)

biblioteca.libros = [mi_libro, mi_libro_no_disponible, otro_libro]

print(biblioteca.libros)