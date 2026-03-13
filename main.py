from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError
from persistencia import Persistencia

persistencia = Persistencia()
biblioteca = persistencia.cargar_datos()

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

persistencia.guardar_datos(biblioteca)



