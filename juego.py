import random
from funciones import *

jugador = {
    "nombre": '',
    "puntaje": '',
    "vidas": '',
    "puntos_ganados": 0,
    "puntos_perdidos": 0 
}

ranking = []

# Ejecución del juego
mostrar_menu()
opcion = ingresar_numero(1, 3)

if opcion == 1:
    jugar_juego()
elif opcion == 2:
    mostrar_rankings()
elif opcion == 3:
    terminar_juego()
else:
    print("Opción no válida.")