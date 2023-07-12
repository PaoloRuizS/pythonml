import random

def obtener_jugada():
    jugada = input("Elige tu jugada (piedra, papel, tijeras): ")
    while jugada not in ["piedra", "papel", "tijeras"]:
        jugada = input("Jugada inválida. Elige piedra, papel o tijeras: ")
    return jugada

def jugar():
    opciones = ["piedra", "papel", "tijeras"]
    jugador = obtener_jugada()
    computadora = random.choice(opciones)
    print("Jugador:", jugador)
    print("Computadora:", computadora)

    if jugador == computadora:
        print("Empate")
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

jugar()