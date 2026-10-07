Equipo 10

- Jhimy Isaac Landaverde Gutiérrez
- Ana Guadalupe Echeverría Guillén
- Joel Esaú Méndez Segura
- Estiven Edgardo Alvarenga Henríquez
- Justin Adonai Lemus Hernández

  Seleccionamos el escenario A

  Se realizo un sistema para una biblioteca de universidad donde hay revistas y libros, utilizando herencias y polimorfismo en python. ademas de eso se creo una pagina web en representación de esta dando a notar como se vería.

  Clase padre
  MaterialBiblioteca: contiene título, código y disponibilidad.

  Clases hijas
  Libro: hereda de MaterialBiblioteca e incorpora el atributo "autor".
  Revista: hereda de MaterialBiblioteca e incorpora el atributo "numero_edicion"

  Métodos sobrescritos
  mostrar_informacion(): cada clase hija muestra su información específica.
  calcular_dias_prestamo(): Libro devuelve 7 días, Revista devuelve 3 días.

  Polimorfismo
  Se crearon 2 libros y 2 revistas, se almacenaron en una misma lista de tipo "MaterialBiblioteca" y se recorrieron. Cada objeto   ejecutó su propia versión de los métodos sobrescritos.

HTML: estructura de la página con catálogo de materiales.
CSS: presentación clara con tarjetas, colores diferenciados por tipo y diseño responsive.
JavaScript: muestra un mensaje al solicitar el préstamo de un material.

Frontend: Mostrar catálogo, permitir seleccionar material y mostrar mensaje de confirmación.
Backend: (conceptual), Validar disponibilidad, registrar el préstamo y calcular días según el tipo de material.
