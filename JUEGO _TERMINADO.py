
#JUEGO DE PIEDRA, PAPEL O TIJERAS

while True:
    print("🪨  📄 ✂ ¡PIEDRA, PAPEL O TIJERAS!\n")
    print("🤩 Bienvenido al juego.")

    opciones = ("piedra", "papel", "tijeras")
    puntos = 0

    while True:
        empezar = input("Escribe 'Jugar' para comenzar o 'SALIR' para abandonarlo:").lower()
        if empezar == "jugar":
            break
        elif empezar == "salir":
            print("👻 Saliste del juego, vuelve pronto.")
            exit()
        else:
            print("Esta opción no es válida, vuelve a tratar.\n")
    print()
    print("🤖 Derrota a la máquina y consigue 10 puntos.")
    print("Llega a 50 puntos y gana.\n")

    while puntos < 50:
        jugador = input("¿Cuál será tu jugada?:").lower()
        if jugador not in opciones:
            print("Escoge una opción válida.\n")
            continue

        import random
        maquina = random.choice(opciones)
        print(f"👾 La computadora escogió:{maquina}")

        if maquina == jugador:
            print("🫤 Es un empate.")
            print("No se suman puntos")
            print(f"💠 Tienes {puntos} puntos.\n")
        elif (jugador == "piedra" and maquina == "tijeras") or \
             (jugador == "papel" and maquina == "piedra") or \
             (jugador == "tijeras" and maquina == "papel"):
            print("😎 Ganaste.")
            puntos += 10
            print(f"💠 Tienes {puntos} puntos.\n")
        else:
            print("😡 Perdiste, sigue intentando.")
            print(f"💠 Tienes {puntos} puntos.\n")
    print("🥳 ¡Felicidades! Le ganaste a la maquina.\n")
    

    again = input("😶‍🌫️ ¿Deseas volver a jugar?:").lower()
    if again == "si":
        continue
    elif again == "no":
        print("Saliste del juego, vuelve pronto.")
        print("👻 Gracias por jugar.")
        exit()
    else:
        print("Esta opción no es válida, vuelve a tratar.\n")