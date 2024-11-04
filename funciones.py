import random
jugador = {
    "nombre": '',
    "puntaje": '',
    "vidas": '',
    "puntos_ganados": 0,
    "puntos_perdidos": 0 
}
ranking = []

def modificar_puntaje(jugador:dict, nuevo_puntaje:int)->bool:
    jugador["puntaje"] += nuevo_puntaje 
    print(f"Puntaje: {jugador["puntaje"]}")

# 2. Modificar vidas del jugador
def modificar_vidas(jugador, cantidad):
    jugador["vidas"] += cantidad
    print(f"Vidas restantes: {jugador['vidas']}")

# 3. Modificar estadísticas del jugador
def modificar_estadistica_jugador(jugador, clave, valor):
    jugador[clave] = valor
    print(f"{clave.capitalize()} actualizado a: {valor}")

# 4. Generar respuesta aleatoria
def generar_respuesta_aleatoria(minimo, maximo):
    return random.randint(minimo, maximo)

# 5. Mezclar lista
def mezclar_lista(lista):
    random.shuffle(lista)
    print("Lista mezclada:", lista)
    return lista

# 6. Obtener elemento aleatorio
def obtener_elemento_aleatorio(coleccion):
    return random.choice(coleccion)

# 7. Agregar dato a diccionario
def agregar_dato(diccionario, clave, valor):
    diccionario[clave] = valor
    print(f"Dato agregado: {clave} = {valor}")

# 8. Mostrar dato del diccionario
def mostrar_dato(diccionario, clave):
    if clave in diccionario:
        print(f"{clave}: {diccionario[clave]}")
    else:
        print(f"{clave} no encontrado.")

# 9. Obtener dato del diccionario
def obtener_dato(diccionario, clave):
    return diccionario.get(clave, "Dato no encontrado")

# 10. Modificar dato en diccionario
def modificar_dato(diccionario, clave, valor):
    if clave in diccionario:
        diccionario[clave] = valor
        print(f"{clave} modificado a {valor}")
    else:
        print(f"{clave} no encontrado.")

# 11. Terminar juego
def terminar_juego():
    print("Gracias por jugar. ¡Hasta la próxima!")

# 12. Guardar puntuación en el ranking
def guardar_puntuacion(jugador):
    ranking.append((jugador["nombre"], jugador["puntaje"]))
    print("Puntuación guardada en el ranking.")

# 13. Ordenar puntuaciones en el ranking
def ordenar_puntuaciones():
    ranking.sort(key=lambda x: x[1], reverse=True)
    print("Ranking ordenado.")

# 14. Mostrar ranking
def mostrar_rankings():
    print("Ranking de jugadores:")
    for i, (nombre, puntaje) in enumerate(ranking, 1):
        print(f"{i}. {nombre} - {puntaje}")

# 15. Ingresar nombre de usuario
def ingresar_nombre_usuario():
    nombre = input("Ingrese su nombre: ")
    jugador["nombre"] = nombre

# Ingresar número entre dos rangos
def ingresar_numero(minimo, maximo):
    numero = input(f"Ingrese un número entre {minimo} y {maximo}: ")
    while not minimo <= numero <= maximo:
        print(f"Por favor, ingrese un número válido entre {minimo} y {maximo}.")
        numero = input(f"Ingrese un número entre {minimo} y {maximo}: ")
    return int(numero)

# 17. Mostrar menú del juego
def mostrar_menu():
    print("1. Iniciar juego")
    print("2. Ver ranking")
    print("3. Salir")

# 18. Calcular porcentaje
def calcular_porcentaje(parte, total):
    if total > 0:
        return (parte / total) * 100
    return 0

# 19. Verificar estado del juego
def verificar_estado_juego(jugador):
    return jugador["vidas"] > 0

# 20. Jugar juego de eliminar zombies
def jugar_juego():
    print("¡Bienvenido al juego de eliminación de zombies!")
    ingresar_nombre_usuario()
    partes_cuerpo = {"cabeza": 100, "torso": 50, "piernas": 20}
    
    while verificar_estado_juego(jugador):
        # Elegir aleatoriamente una parte del cuerpo a disparar
        parte_disparada = obtener_elemento_aleatorio(list(partes_cuerpo.keys()))
        puntos = partes_cuerpo[parte_disparada]
        
        print(f"Disparaste al zombie en la {parte_disparada}. ¡Ganaste {puntos} puntos!")
        modificar_puntaje(jugador, puntos)
        
        # Descontar una vida en cada ronda
        modificar_vidas(jugador, -1)
    
    guardar_puntuacion(jugador)
    terminar_juego()

