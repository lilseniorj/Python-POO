from biblioteca import Biblioteca
from data import data_estudiantes, data_libros
from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError
from usuarios import Profesor
from libros import Libro

biblioteca = Biblioteca("Platzi Biblioteca")
profesor = Profesor("Luis", "4123123")


biblioteca.usuarios = [profesor] + data_estudiantes
biblioteca.libros = list(data_libros)

# libro_de_prueba = data_libros[0]
# libro_de_prueba.veces_prestado = -1
libro_no_disponible = Libro.crear_no_disponible(
    "Libro de prieba", "Author de prueba", "23423523"
)
print("Libro disponibles:", libro_no_disponible.disponible)


print("Bienvenido a lil Biblioteca")

print("Libros disponibles: ")
for libro in biblioteca.libros_disponibles():
    print(libro.descripcion_completa)
print()

id = input("Digite el numero de cedula: ")
try:
    usuario = biblioteca.buscar_usuario(id)
    print(usuario.id, usuario.name)
except UsuarioNoEncontradoError as e:
    print(e)


titulo = input("Digite el titulo del libro: ")
try:
    libro = biblioteca.buscar_libro(titulo)
    print(f"El libro que seleccionaste es: {libro}")
except LibroNoDisponibleError as e:
    print(e)


resultado = usuario.solicitar_libro(libro.titulo)
print(f"\n{resultado}" )

try:
    resultado_prestar = libro.prestar()
    print(f"\n{resultado_prestar}" )
except LibroNoDisponibleError as e:
    print(e)


# resultado = Biblioteca.validar_isbn("1232312312")
# print(f"EL ISBN es valido: {resultado}")

