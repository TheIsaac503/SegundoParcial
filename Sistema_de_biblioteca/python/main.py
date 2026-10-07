"""
Escenario A - Sistema de Biblioteca Universitaria
Demostración de herencia y polimorfismo
"""

from modelos import MaterialBiblioteca, Libro, Revista


def main():
    print("=" * 70)
    print("       SISTEMA DE BIBLIOTECA UNIVERSITARIA")
    print("       Demostración de Herencia y Polimorfismo")
    print("=" * 70)
    print()

    # Crear al menos dos libros y dos revistas
    libro1 = Libro(
        titulo="Cien años de soledad",
        codigo="LIB-001",
        autor="Gabriel García Márquez",
        disponible=True
    )

    libro2 = Libro(
        titulo="El Principito",
        codigo="LIB-002",
        autor="Antoine de Saint-Exupéry",
        disponible=True
    )

    revista1 = Revista(
        titulo="National Geographic",
        codigo="REV-001",
        numero_edicion=248,
        disponible=True
    )

    revista2 = Revista(
        titulo="Muy Interesante",
        codigo="REV-002",
        numero_edicion=512,
        disponible=False
    )

    # Almacenar todos los materiales en una misma colección (lista)
    catalogo: list[MaterialBiblioteca] = [libro1, libro2, revista1, revista2]

    print("CATÁLOGO DE MATERIALES")
    print("-" * 70)

    # Recorrer la colección utilizando polimorfismo
    # Cada objeto ejecuta su propia versión de mostrar_informacion()
    # y calcular_dias_prestamo() según su tipo real (Libro o Revista)
    for material in catalogo:
        print(material.mostrar_informacion())
        print(f"   → Días de préstamo calculados: {material.calcular_dias_prestamo()}")
        print()

    print("=" * 70)
    print("Explicación del polimorfismo:")
    print("Se recorrió una lista de tipo MaterialBiblioteca.")
    print("Aunque todos se tratan como la clase padre, cada objeto")
    print("ejecutó su propio método sobrescrito (Libro o Revista).")
    print("=" * 70)


if __name__ == "__main__":
    main()
