#Parte Python

class MaterialBiblioteca:
    def __init__(self, titulo, codigo, disponible=True):
        self.titulo = titulo
        self.codigo = codigo
        self.disponible = disponible

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"[{self.codigo}] {self.titulo} — Estado: {estado}"

    def calcular_dias_prestamo(self):
        return 0


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, codigo, autor, disponible=True):
        super().__init__(titulo, codigo, disponible)
        self.autor = autor

    def mostrar_informacion(self):
        return f"Libro: {super().mostrar_informacion()} | Autor: {self.autor}"

    def calcular_dias_prestamo(self):
        return 7


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, codigo, numero_edicion, disponible=True):
        super().__init__(titulo, codigo, disponible)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        return f"Revista: {super().mostrar_informacion()} | Edición Nº: {self.numero_edicion}"

    def calcular_dias_prestamo(self):
        return 3


if __name__ == "__main__":
    catalogo = [
        Libro("Cien Años de Soledad", "LIB-001", "Gabriel García Márquez"),
        Libro("Don Quijote de la Mancha", "LIB-002", "Miguel de Cervantes", disponible=False),
        Revista("National Geographic", "REV-101", 245),
        Revista("Scientific American", "REV-102", 112)
    ]

    print("=" * 45)
    print(" SISTEMA DE BIBLIOTECA - CATÁLOGO ")
    print("=" * 45 + "\n")

    for material in catalogo:
        print(material.mostrar_informacion())
        print(f" Días de préstamo: {material.calcular_dias_prestamo()} días\n")