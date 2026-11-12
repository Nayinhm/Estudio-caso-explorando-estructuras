
class Material:
    """Clase que representa un material bibliográfico en la biblioteca."""
    def __init__(self, codigo, titulo, autor, estado="disponible"):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.estado = estado  # "disponible" o "prestado"

    def __str__(self):
        return f"Código: {self.codigo} | Título: '{self.titulo}' | Autor: {self.autor} | Estado: {self.estado}"