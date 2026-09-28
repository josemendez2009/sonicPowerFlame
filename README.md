# sonicPowerFlame
sonic power flames; esquiva, apaga llamas encuentra armas usalas contra los jefes y desarrolla estrategias con tus amigos Jugable para la terminal de visual studio code

#José Luis Mendez Rojas 
soy programador JR. con conocimientos y buenas practicas en POO.

#FASE 1. Analisis escrito
en la parte de codigo encontrará el analisis escrito de como se espera que sea el juego con datos importantes en el para el desarrollo de su respectivo diagrama de flujo

#FASE 2. Diagrama de flujo del juego
en la parte de codigo se encuentra el respectivo diagrama de flujo que se hizo despues del analisis que indica las direcciones los mundos los apartados (vestuario, personajes, herramientas, etc) junto con lo que todavia se necesita terminar del juego

#Fase 3. Codigo en VISUAL STUDIO CODE en lenguaje de python jugable para la consola de visual
es el codigo en donde el videojuego toma vida y en donde se cumple todo lo del analisis y diagrama de flujo

#Fase 4. reprositorio en github
en github creamos un repositorio interactivo que permita qu todo lo que hagamos se pueda editar exportar y compartir con otros usuarios y jugadores

# PARTES DEL JUEGO
#Importaciones
import os, sys, time y random son las librerías estándar empleadas para manipular comandos de la consola, interactuar con el sistema, pausar y medir tiempos de ejecución, y generar eventos o elementos aleatorios como obstáculos y disparos. Además, se realiza una importación condicional en un bloque try/except donde se intenta cargar msvcrt para sistemas Windows o select, tty y termios para sistemas basados en Unix/Linux, permitiendo capturar teclas en tiempo real sin necesidad de presionar Enter.
#Variables
nivel_2_desbloqueado y mundo_2_desbloqueado son variables globales booleanas encargadas de controlar el progreso de desbloqueo de pantallas. Dentro de las funciones de cada nivel destacan variables numéricas y de posición como carril_sonic, altura_sonic, tiempo_salto, fila_jugador, fila_jefe y vida_jefe, constantes de configuración como ANCHO_PISTA, ALTO_MAPA, distancia_meta y DURACION_MAXIMA, variables de tiempo como tiempo_inicio y tiempo_restante, matrices para la grilla del juego como pista, y estructuras de listas como balas_jugador y balas_jefe para almacenar las coordenadas de los proyectiles en movimiento. En el menú principal también se capturan entradas del usuario en variables como nombre y opcion.
#Funciones
obtener_tecla() detecta y retorna la tecla presionada de forma no bloqueante según el sistema operativo detectado; limpiar() ejecuta el comando de borrado de pantalla (cls o clear); jugar_nivel_1() administra la lógica de carrera, desplazamiento de pista de abajo hacia arriba, generación de obstáculos "X", tiempo límite e interacciones en tiempo real; jugar_nivel_2() gestiona el combate contra un jefe (W), incluyendo la lógica de física e impacto de los disparos hacia arriba (|) y descendentes (v), salud del enemigo y derrota por tiempo o daño; y finalmente modulo_jugar() actúa como submenú interactivo para seleccionar entre los niveles disponibles y manejar la opción de reintentar si el jugador pierde.
#Estructuras de Control
El código implementa bucles while True para mantener activos los ciclos de refresco de pantalla (game loop) en cada nivel, los reintentos de pantalla y la navegación continua del menú principal sin cerrar el programa. A su vez, se valora el uso de sentencias if, elif y else para evaluar los controles por teclado (como 'a', 'd', 'w', 'f', 'j' y 'q'), validar las colisiones de coordenadas en la matriz, comprobar la vida restante del jefe, controlar el tiempo transcurrido y gestionar la navegación de las distintas opciones del menú principal.
#Estructura General del Programa
El programa organiza su flujo iniciando con la preparación del entorno (importaciones e interfaz para la lectura de teclado), seguido por la declaración de funciones auxiliares y módulos de nivel, continuando con un submenú de selección de mapas (modulo_jugar) y finalizando en un bloque ejecutable principal que le da la bienvenida al usuario, solicita su nombre y despliega el menú central del juego, desde el cual se redirige secuencialmente a los módulos de juego, secciones decorativas en desarrollo (como taller de atuendos o guardado en la nube) o el cierre del script.
