class Usuario:
	def __init__(self, name, id):
		self.name = name
		self.id = id
		self.libros_prestados = []

	def solicitar_libro(self, titulo):
		return f"La solicitud del libro {titulo} realizada"


class Estudiante(Usuario):
	def __init__(self, name, id, carrera):
		super().__init__(name, id)
		self.carrera = carrera
		self.limite_libros = 3

	def solicitar_libro(self, titulo):
		if len(self.libros_prestados) < self.limite_libros:
			self.libros_prestados.append(titulo)
			return f"Prestamo del libro: {titulo} autorizado"
		else:
			return (
				f"No puedes prestar mas libro, Limite alcanzado {self.limite_libros}"
			)
	def devolver_libro(self, titulo):
		if titulo in self.libros_prestados:
			self.libros_prestados.remove(titulo)
			self.limite_libros -= 1
			return f"El libro {titulo} ha sido devuelto exitosamente, su limite de libros ahora es de {self.limite_libros}, sus libros prestados son {self.libros_prestados}"
		else:
			return f"Este libro {titulo} no esta en su lista de libros prestados, devolución rechazada"

class Profesor(Usuario):
	def __init__(self, name, id):
		super().__init__(name, id)
		self.limite_libros = None

	def solicitar_libro(self, titulo):
		self.libros_prestados.append(titulo)
		return f"Prestamo del libro: {titulo} autorizado"



estudiante = Estudiante("Jesus", "123456", "Sistema")
profesor = Profesor("Luis", "4123123")

print(profesor.solicitar_libro("Python Basico"))
print(profesor.solicitar_libro("Python Medio"))
print(profesor.solicitar_libro("Python Profesional"))
print(profesor.solicitar_libro("Python Experto"))
print(estudiante.devolver_libro("Python Basico"))


