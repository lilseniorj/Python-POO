from typing import Protocol

class SolicitanteProtocol(Protocol):
	def  solicitar_libro(self, titulo: str) -> str:
		"""Metodo que debe implementar cualquier solicitante"""
		...

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

class Profesor(Usuario):
	def __init__(self, name, id):
		super().__init__(name, id)
		self.limite_libros = None

	def solicitar_libro(self, titulo):
		self.libros_prestados.append(titulo)
		return f"Prestamo del libro: {titulo} autorizado"
