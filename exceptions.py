class BibliotecaError(Exception):
  """Excepción base para errores de la biblioteca"""

  pass


class LimitePrestamosError(BibliotecaError):
  """Se excedió el límite de prestamos permitidos"""

  pass


class TituloInvalidoError(BibliotecaError):
  """El titulo del libro no es valido"""

  pass


class LibroNoDisponibleError:
  """El libro no esta disponible para préstamo"""

  pass


class UsuarioNoEncontradoError(Exception):
  """El usuario no fue encontrado en el sistema"""

  pass