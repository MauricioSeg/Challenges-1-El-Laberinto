# --- Matix Inical ---
import random

espacio_vacio = " "
gato = "😾"
raton = "🐀"

def creacion_tablero (filas, columnas, ubi_gato, ubi_raton):
    # listas de listas para realizar la matix
    
    tablero = [[espacio_vacio for _ in range (columnas)] for _ in range (filas)]
    tablero [ubi_gato][0][ubi_gato][1] = gato
    tablero [ubi_raton][0][ubi_raton][1] = raton
    return tablero

def posiciones_random (filas, columnas):
    # Genrar posiciones alatorias entre el gato y el raton
    
    ubi_gato = (random.randint (0, filas -1), random.randint(0, columnas -1)) 

    while True: 
        ubi_raton = (random.randint(0, filas -1), random.randint(0, columnas -1))
        
        if ubi_raton != ubi_gato:
            break
    
    return ubi_gato, ubi_raton