
#JUEGO DE PIEDRA, PAPEL O TIJERAS

opciones = ("piedra","papel","tijeras")
jugador = input("¿Cuál será tu jugada?:")

import random
maquina = random.choice (opciones)
print("La computadora seleccionó:",maquina)

if maquina == jugador:
    print("empate")
elif (jugador== "piedra" and maquina== "tijeras") or \
    (jugador== "papel" and maquina== "piedra") or \
    (jugador== "tijeras" and maquina== "papel"):
    print("Ganaste")
else:
    print("Perdiste")