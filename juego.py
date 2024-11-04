from funciones import *

# Ejecución del juego
salir = ''
while salir != terminar_juego() :
    mostrar_menu()
    opcion = ingresar_numero(1, 3)
    if opcion == 1:
        jugar_juego()
    elif opcion == 2:
        mostrar_rankings()
    elif opcion == 3:
        salir = terminar_juego()
    else:
        print("Opción no válida.")