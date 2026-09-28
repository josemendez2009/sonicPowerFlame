import os
import sys
import time
import random

# Detectar el sistema operativo para la lectura de teclas en tiempo real
try:
    import msvcrt
    def obtener_tecla():
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8', errors='ignore').lower()
        return None
except ImportError:
    import select
    import tty
    import termios
    def obtener_tecla():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            rlist, _, _ = select.select([sys.stdin], [], [], 0.02)
            if rlist:
                tecla = sys.stdin.read(1).lower()
                return tecla
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Variables globales de progreso
nivel_2_desbloqueado = False
mundo_2_desbloqueado = False

# ----------------- LÓGICA DEL NIVEL 1 -----------------
def jugar_nivel_1():
    global nivel_2_desbloqueado
    limpiar()
    print("====================================================================")
    print("                       INICIANDO NIVEL 1                            ")
    print("====================================================================")
    print(" OBJETIVO: Recorrer la distancia antes de que se agote el tiempo (60s)")
    print(" CONTROLES:")
    print("   [A] -> Mover Izquierda")
    print("   [D] -> Mover Derecha")
    print("   [W] o [Espacio] -> Saltar")
    print("   [Q] -> Salir del Nivel")
    print("\n ¡Presiona ENTER para empezar a correr!")
    input()

    ANCHO_PISTA = 7
    carril_sonic = 3
    altura_sonic = 0
    tiempo_salto = 0
    
    distancia_meta = 50
    distancia_recorrida = 0
    
    pista = [[" " for _ in range(ANCHO_PISTA)] for _ in range(12)]
    
    tiempo_inicio = time.time()
    DURACION_MAXIMA = 60  # 1 minuto

    while True:
        tiempo_transcurrido = time.time() - tiempo_inicio
        tiempo_restante = max(0, int(DURACION_MAXIMA - tiempo_transcurrido))

        if tiempo_restante <= 0:
            limpiar()
            print("\n" + "="*40)
            print("       ¡¡ SE AGOTÓ EL TIEMPO !!")
            print("           PERDISTE EL NIVEL")
            print("="*40)
            time.sleep(1.5)
            return False

        tecla = obtener_tecla()
        if tecla == 'a' and carril_sonic > 0:
            carril_sonic -= 1
        elif tecla == 'd' and carril_sonic < ANCHO_PISTA - 1:
            carril_sonic += 1
        elif (tecla == 'w' or tecla == ' ') and altura_sonic == 0:
            altura_sonic = 1
            tiempo_salto = 3
        elif tecla == 'q':
            print("\nHas salido del nivel.")
            time.sleep(1)
            return False

        if altura_sonic == 1:
            tiempo_salto -= 1
            if tiempo_salto <= 0:
                altura_sonic = 0

        # Generar pista aleatoria
        nueva_fila = [" " for _ in range(ANCHO_PISTA)]
        if random.random() < 0.35:
            pos_obstaculo = random.randint(0, ANCHO_PISTA - 1)
            nueva_fila[pos_obstaculo] = "X"
            
        pista.pop(0)
        pista.append(nueva_fila)

        distancia_recorrida += 1
        fila_jugador = 2
        
        # Colisión con obstáculo
        if pista[fila_jugador][carril_sonic] == "X" and altura_sonic == 0:
            limpiar()
            print("\n" + "="*40)
            print("     ¡¡ CHOCASTE CON UN OBSTÁCULO !!")
            print("           PERDISTE EL NIVEL")
            print("="*40)
            time.sleep(1.5)
            return False

        if distancia_recorrida >= distancia_meta:
            limpiar()
            print("\n" + "="*40)
            print("   ¡¡ FELICIDADES! GANASTE EL NIVEL 1 !!")
            print("="*40)
            nivel_2_desbloqueado = True
            print("\n [!] ¡Nivel 2 Desbloqueado!")
            input("\nPresiona Enter para continuar...")
            return True

        # Renderizado
        limpiar()
        print(f"--- SONIC POWER FLAMES | NIVEL 1 ---")
        print(f"Progreso: {distancia_recorrida}/{distancia_meta}m | Tiempo Restante: {tiempo_restante}s")
        print("+" + "-" * ANCHO_PISTA + "+")
        
        for idx_fila in range(len(pista) - 1, -1, -1):
            linea = ""
            for idx_col in range(ANCHO_PISTA):
                if idx_fila == fila_jugador and idx_col == carril_sonic:
                    linea += "^" if altura_sonic == 1 else "•"
                else:
                    linea += pista[idx_fila][idx_col]
            print("|" + linea + "|")
            
        print("+" + "-" * ANCHO_PISTA + "+")
        print(" Controles: A (Izq) | D (Der) | W/Espacio (Saltar) | Q (Salir)")
        
        time.sleep(0.18)


# ----------------- LÓGICA DEL NIVEL 2 (JEFE) -----------------
def jugar_nivel_2():
    limpiar()
    print("====================================================================")
    print("                 INICIANDO NIVEL 2 - BATALLA CON EL JEFE            ")
    print("====================================================================")
    print(" OBJETIVO: ¡Dispara al Jefe 3 veces antes de que se agote el tiempo (60s)!")
    print(" CONTROLES:")
    print("   [A] / [D]     -> Mover Izquierda / Derecha")
    print("   [W] / Espacio -> Saltar")
    print("   [F] o [J]     -> Disparar hacia adelante")
    print("   [Q]           -> Salir del Nivel")
    print("\n ¡Presiona ENTER para empezar la batalla!")
    input()

    ANCHO_PISTA = 7
    ALTO_MAPA = 12
    carril_sonic = 3
    altura_sonic = 0
    tiempo_salto = 0
    
    vida_jefe = 3
    fila_jugador = 1
    fila_jefe = ALTO_MAPA - 1

    # Listas de proyectiles: [fila, columna]
    balas_jugador = []
    balas_jefe = []

    tiempo_inicio = time.time()
    DURACION_MAXIMA = 60

    while True:
        tiempo_transcurrido = time.time() - tiempo_inicio
        tiempo_restante = max(0, int(DURACION_MAXIMA - tiempo_transcurrido))

        if tiempo_restante <= 0:
            limpiar()
            print("\n" + "="*40)
            print("       ¡¡ SE AGOTÓ EL TIEMPO !!")
            print("         EL JEFE HA GANADO")
            print("="*40)
            time.sleep(1.5)
            return False

        # Leer controles
        tecla = obtener_tecla()
        if tecla == 'a' and carril_sonic > 0:
            carril_sonic -= 1
        elif tecla == 'd' and carril_sonic < ANCHO_PISTA - 1:
            carril_sonic += 1
        elif (tecla == 'w' or tecla == ' ') and altura_sonic == 0:
            altura_sonic = 1
            tiempo_salto = 3
        elif tecla in ['f', 'j']:
            # Jugador dispara una bala
            balas_jugador.append([fila_jugador + 1, carril_sonic])
        elif tecla == 'q':
            print("\nHas salido del nivel.")
            time.sleep(1)
            return False

        if altura_sonic == 1:
            tiempo_salto -= 1
            if tiempo_salto <= 0:
                altura_sonic = 0

        # Disparo aleatorio del Jefe
        if random.random() < 0.4:
            carril_disparo_jefe = random.randint(0, ANCHO_PISTA - 1)
            balas_jefe.append([fila_jefe - 1, carril_disparo_jefe])

        # Mover balas del jugador hacia arriba
        nuevas_balas_jugador = []
        for b in balas_jugador:
            b[0] += 1  # sube una fila
            if b[0] == fila_jefe:  # Impacta en el jefe
                vida_jefe -= 1
            elif b[0] < fila_jefe:
                nuevas_balas_jugador.append(b)
        balas_jugador = nuevas_balas_jugador

        # Mover balas del jefe hacia abajo
        nuevas_balas_jefe = []
        for b in balas_jefe:
            b[0] -= 1  # baja una fila
            # Verificar si la bala toca al jugador
            if b[0] == fila_jugador and b[1] == carril_sonic and altura_sonic == 0:
                limpiar()
                print("\n" + "="*40)
                print("      ¡¡ TE ALCANZÓ EL DISPARO DEL JEFE !!")
                print("               PERDISTE EL NIVEL")
                print("="*40)
                time.sleep(1.5)
                return False
            elif b[0] >= 0:
                nuevas_balas_jefe.append(b)
        balas_jefe = nuevas_balas_jefe

        # Verificar victoria contra el jefe
        if vida_jefe <= 0:
            limpiar()
            print("\n" + "="*40)
            print("   ¡¡ FELICIDADES! DERROTASTE AL JEFE !!")
            print("      ¡¡ HAS COMPLETADO EL MUNDO 1 !!")
            print("="*40)
            input("\nPresiona Enter para continuar...")
            return True

        # Renderizar mapa de combate
        limpiar()
        print(f"--- SONIC POWER FLAMES | NIVEL 2 (JEFE) ---")
        print(f"Vida del Jefe: {'❤️ '*vida_jefe} | Tiempo Restante: {tiempo_restante}s")
        print("+" + "-" * ANCHO_PISTA + "+")

        for f in range(ALTO_MAPA - 1, -1, -1):
            linea = ""
            for c in range(ANCHO_PISTA):
                if f == fila_jefe and c == 3:
                    linea += "W"  # Icono del Jefe
                elif f == fila_jugador and c == carril_sonic:
                    linea += "^" if altura_sonic == 1 else "•"
                else:
                    # Comprobar proyectiles en esta casilla
                    hay_bala_jefe = any(b[0] == f and b[1] == c for b in balas_jefe)
                    hay_bala_jugador = any(b[0] == f and b[1] == c for b in balas_jugador)
                    
                    if hay_bala_jefe:
                        linea += "v"  # Disparo descendente
                    elif hay_bala_jugador:
                        linea += "|"  # Disparo ascendente
                    else:
                        linea += " "
            print("|" + linea + "|")

        print("+" + "-" * ANCHO_PISTA + "+")
        print(" Controles: A (Izq) | D (Der) | W (Saltar) | F/J (Disparar)")

        time.sleep(0.15)


def modulo_jugar():
    global nivel_2_desbloqueado
    while True:
        limpiar()
        print("====================================================================")
        print("                           MAPA (MUNDO 1)                           ")
        print("====================================================================")
        print(" 1. Nivel 1 [Disponible]")
        if nivel_2_desbloqueado:
            print(" 2. Nivel 2 - Batalla contra el Jefe [Disponible]")
        else:
            print(" 2. Nivel 2 [Bloqueado 🔒]")
        print(" M. Regresar al Menú Principal")
        print("====================================================================")
        
        opc_mapa = input("Selecciona una opción: ").strip().lower()

        if opc_mapa == "1":
            while True:
                gano = jugar_nivel_1()
                if not gano:
                    reiniciar = input("\n¿Deseas reiniciar el Nivel 1? (S/N): ").strip().lower()
                    if reiniciar == 's':
                        continue
                    else:
                        break
                else:
                    break

        elif opc_mapa == "2":
            if nivel_2_desbloqueado:
                while True:
                    gano = jugar_nivel_2()
                    if not gano:
                        reiniciar = input("\n¿Deseas reiniciar el Nivel 2? (S/N): ").strip().lower()
                        if reiniciar == 's':
                            continue
                        else:
                            break
                    else:
                        break
            else:
                print("\nEl Nivel 2 está bloqueado. Debes completar el Nivel 1 primero.")
                input("Presiona Enter para continuar...")

        elif opc_mapa == "m":
            break


# ----------------- CÓDIGO PRINCIPAL / MENÚ -----------------

limpiar()
print("--- cargando ---")
nume = input("Toca Enter para empezar: ")
limpiar()
print("\n--------------------------------- BIENVENIDO --------------------------")
print("------------------------ SONIC POWER FLAMES ---------------------")
nuo = input("Iniciar: ")
limpiar()
print("------------------------ SONIC POWER FLAMES ---------------------")
nombre = input("Ingresa tu nombre: ")
iniciar = input(f"\nQué nombre más cool {nombre}, ¿listo para empezar? (Press Enter): ")

while True:
    limpiar()
    print("====================================================================")
    print(f"                     SONIC POWER FLAMES - MENÚ                      ")
    print(f" Jugador: {nombre}")
    print("====================================================================")
    print(" [ENTER] -> Jugar (Mapa / Mundo 1)")
    print(" [M]     -> Mundo 2 (Mapa Bloqueado 🔒)")
    print(" [V]     -> Vestimenta / Taller de Atuendos")
    print(" [P]     -> Personajes / Galería de Atuendos")
    print(" [N]     -> Inicio de Sesión / Guardado en la Nube")
    print(" [O]     -> Opciones (Notificaciones, Créditos, Info Legal)")
    print(" [S]     -> Salir del Juego")
    print("====================================================================")
    
    opcion = input("Selecciona una opción: ").strip().lower()

    if opcion == "":
        modulo_jugar()

    elif opcion == "m":
        limpiar()
        print("====================================================================")
        print("                           MAPA (MUNDO 2)                           ")
        print("====================================================================")
        print("\n [🔒] El Mundo 2 está bloqueado actualmente.")
        input("\nPresiona Enter para regresar al Menú...")

    elif opcion == "v":
        limpiar()
        print("====================================================================")
        print("                       TALLER DE ATUENDOS                           ")
        print("====================================================================")
        print("1. Ver Objetos y Power-ups")
        print("2. Adquirir Atuendo del Personaje")
        print("3. Cambiar Atuendo")
        print("[Módulo en desarrollo...]")
        input("\nPresiona Enter para regresar al Menú...")

    elif opcion == "p":
        limpiar()
        print("====================================================================")
        print("                        GALERÍA DE PERSONAJES                       ")
        print("====================================================================")
        print("- Traje: Sonic Flame")
        print("- Traje: Amy Rose Dress")
        print("- Traje: Shadow Armour")
        print("[Módulo en desarrollo...]")
        input("\nPresiona Enter para regresar al Menú...")

    elif opcion == "n":
        limpiar()
        print("====================================================================")
        print("                     GUARDADO / CARGA EN LA NUBE                    ")
        print("====================================================================")
        confirmar = input("¿Está seguro de cargar/guardar datos en la Nube? (Si/No): ")
        print(f"Procesando opción: {confirmar}...")
        input("\nPresiona Enter para regresar al Menú...")

    elif opcion == "o":
        limpiar()
        print("====================================================================")
        print("                              OPCIONES                              ")
        print("====================================================================")
        print("1. Notificaciones (Apagar: Sí / No)")
        print("2. Créditos (Ver créditos)")
        print("3. Información legal (Ver información legal)")
        print("4. Pedir soporte / Contactarse")
        input("\nPresiona Enter para regresar al Menú...")

    elif opcion == "s":
        limpiar()
        print("¡Gracias por jugar Sonic Power Flames! Hasta pronto.")
        break

    else:
        print("Opción no válida. Presiona Enter e intenta de nuevo.")
        input()