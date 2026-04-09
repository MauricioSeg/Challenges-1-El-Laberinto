import random
import time

# Tamaño de la matrix (Tablero) y configuraciones basicas del juego 
filas = 5
columnas = 5
turnos_maximos = 20
profundidad = 3

# Funcion para generar ubicaciones random para el gato y el raton
def generar_posiciones():
    todas_las_posiciones = [[fila, col]
                            for fila in range(filas)
                            for col in range(columnas)]
    
    pos_inicial = random.sample(todas_las_posiciones, 2)
    return pos_inicial[0], pos_inicial[1]


# Muestra el tablero en consola con los personajes
def mostrar_tablero(gato, raton, turno): 
    print(f"\n--- Turno {turno} ---") 
    for fila in range(filas):
        linea = "  "
        for col in range(columnas):
            posicion_actual = [fila, col]
            if posicion_actual == gato and posicion_actual == raton:
                linea += "💥 "
            elif posicion_actual == gato:
                linea += "🐱 "
            elif posicion_actual == raton:
                linea += "🐭 "
            else:
                linea += "·  "
        print(linea)


# Compara si dos posiciones son iguales 
def misma_posicion(a, b):
    return a[0] == b[0] and a[1] == b[1]


# Calcula la distancia entre dos posiciones
def calcular_distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Devuelve los movimientos posibles desde una posicion
def movimientos_posibles(posicion):
    fila, col = posicion
    movimientos = []
    for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nueva_fila = fila + df
        nueva_col  = col + dc
        if 0 <= nueva_fila < filas and 0 <= nueva_col < columnas:
            movimientos.append([nueva_fila, nueva_col])
    return movimientos


# Algoritmo minimax - el gato minimiza, el raton maximiza
def minimax(gato, raton, profundidad_actual, turno_del_gato):
    # Si el gato atrapo al raton, termina
    if misma_posicion(gato, raton):
        return -1000

    # Si llegamos al limite de profundidad, evaluamos la distancia
    if profundidad_actual == 0:
        return calcular_distancia(gato, raton)

    if turno_del_gato:
        mejor_valor = 9999
        for movimiento in movimientos_posibles(gato):
            valor = minimax(movimiento, raton, profundidad_actual - 1, False)
            if valor < mejor_valor:
                mejor_valor = valor
        return mejor_valor
    else:
        mejor_valor = -9999
        for movimiento in movimientos_posibles(raton):
            valor = minimax(gato, movimiento, profundidad_actual - 1, True)
            if valor > mejor_valor:
                mejor_valor = valor
        return mejor_valor


# El gato elige el mejor movimiento usando minimax
def mover_gato(gato, raton):
    mejor_movimiento = None
    mejor_valor = 9999

    for movimiento in movimientos_posibles(gato):
        valor = minimax(movimiento, raton, profundidad - 1, False)
        if valor < mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento

    return mejor_movimiento


# El raton elige el mejor movimiento usando minimax
def mover_raton(gato, raton):
    mejor_movimiento = None
    mejor_valor = -9999

    for movimiento in movimientos_posibles(raton):
        valor = minimax(gato, movimiento, profundidad - 1, True)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento

    return mejor_movimiento


# --- Inicio del juego ---
posicion_gato, posicion_raton = generar_posiciones()

print("🧪 Simulacion Minimax — Gato vs Raton")
print(f"🐱 Gato arranca en:  {posicion_gato}")
print(f"🐭 Raton arranca en: {posicion_raton}")

for turno in range(1, turnos_maximos + 1):
    mostrar_tablero(posicion_gato, posicion_raton, turno)
    time.sleep(0.5)

    # Turno del gato
    posicion_gato = mover_gato(posicion_gato, posicion_raton)
    if misma_posicion(posicion_gato, posicion_raton):
        mostrar_tablero(posicion_gato, posicion_raton, turno)
        print("\n🐱 El gato atrapo al raton! Gana el GATO. 😈")
        break

    # Turno del raton
    posicion_raton = mover_raton(posicion_gato, posicion_raton)
    if misma_posicion(posicion_gato, posicion_raton):
        mostrar_tablero(posicion_gato, posicion_raton, turno)
        print("\n🐱 El gato atrapo al raton! Gana el GATO. 😈")
        break

else:
    mostrar_tablero(posicion_gato, posicion_raton, turnos_maximos)
    print("\n🐭 El raton sobrevivio! Gana el RATON. 🎉")

input("\nPresiona Enter para finalizar...")