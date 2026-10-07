/**
 * Sistema de Biblioteca Universitaria
 * Escenario A - Evaluación Práctica POO
 * Manejo de interacción del usuario al solicitar préstamo
 */

/**
 * Función principal que se ejecuta al hacer clic en "Solicitar préstamo"
 * @param {HTMLButtonElement} boton - El botón que fue presionado
 */
function solicitarPrestamo(boton) {
    // Obtenemos la tarjeta (article) que contiene el botón
    const tarjeta = boton.closest('.tarjeta');

    // Extraemos la información del material desde los atributos data-*
    const tipo = tarjeta.dataset.tipo;
    const titulo = tarjeta.dataset.titulo;
    const codigo = tarjeta.dataset.codigo;
    const disponible = tarjeta.dataset.disponible === 'true';

    // Referencia al contenedor del mensaje
    const mensaje = document.getElementById('mensaje');

    // Si el material no está disponible
    if (!disponible) {
        mostrarMensaje(
            `El material "${titulo}" (${codigo}) no se encuentra disponible en este momento.`,
            'error'
        );
        return;
    }

    // Determinamos los días de préstamo según el tipo (polimorfismo conceptual)
    const diasPrestamo = tipo === 'Libro' ? 7 : 3;

    // Mensaje de éxito
    const texto = `¡Préstamo solicitado con éxito!\n` +
                  `Material: ${titulo}\n` +
                  `Tipo: ${tipo} | Código: ${codigo}\n` +
                  `Días de préstamo: ${diasPrestamo}`;

    mostrarMensaje(texto, 'exito');
}

/**
 * Muestra un mensaje temporal en pantalla
 * @param {string} texto - Contenido del mensaje
 * @param {string} tipo - 'exito' o 'error'
 */
function mostrarMensaje(texto, tipo) {
    const mensaje = document.getElementById('mensaje');

    // Limpiamos clases anteriores y aplicamos la nueva
    mensaje.className = 'mensaje';
    mensaje.classList.add(tipo);
    mensaje.innerText = texto;

    // Mostramos el mensaje
    mensaje.classList.remove('oculto');

    // Ocultamos el mensaje automáticamente después de 4 segundos
    setTimeout(() => {
        mensaje.classList.add('oculto');
    }, 4000);
}
