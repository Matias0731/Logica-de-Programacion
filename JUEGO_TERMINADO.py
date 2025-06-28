

#JUEGO DE PIEDRA, PAPEL O TIJERAS

while True:
    print("\n🪨  📄 ✂ ¡PIEDRA, PAPEL O TIJERAS!\n")
    print("🤩 Bienvenido al juego.")

    opciones = ("piedra", "papel", "tijeras")
    puntos = 0
    puntos_maquina = 0

    while True:
        empezar = input("Escribe 'Jugar' para comenzar o 'SALIR' para abandonarlo:").lower()
        if empezar == "jugar":
            break
        elif empezar == "salir":
            print("👻 Saliste del juego, vuelve pronto.")
            exit()
        else:
            print("❌ Esta opción no es válida, vuelve a tratar.\n")
    print()
    print("🤖 Derrota a la máquina y consigue 10 puntos.")
    print("El primero en llegar a 50 puntos gana.\n")

    while puntos <50 and puntos_maquina <50:
        jugador = input("¿Cuál será tu jugada?:").lower()
        if jugador not in opciones:
            print("❌ Esta opción no es válida, vuelve a tratar.\n")
            continue

        import random
        maquina = random.choice(opciones)
        print(f"👾 La computadora escogió:{maquina}")

        if maquina == jugador:
            print("🫤 Es un empate.")
            print("No se suman puntos")
            print(f"💠 Tienes {puntos} puntos.")
            print(f"🖥️  La máquina tiene {puntos_maquina} puntos.\n")
        elif (jugador == "piedra" and maquina == "tijeras") or \
             (jugador == "papel" and maquina == "piedra") or \
             (jugador == "tijeras" and maquina == "papel"):
            print("😎 Ganaste.")
            puntos += 10
            print(f"💠 Tienes {puntos} puntos.")
            print(f"🖥️  La máquina tiene {puntos_maquina} puntos.\n")
        else:
            print("😡 Perdiste, sigue intentando.")
            puntos_maquina +=10
            print(f"💠 Tienes {puntos} puntos.")
            print(f"🖥️  La máquina tiene {puntos_maquina} puntos.\n")

    if puntos_maquina == 50:
        print("😵 Perdiste, la máquina te ganó.")
    else:
        print("🥳 ¡Le ganaste a la máquina!")
        

    again = input("😶‍🌫️ ¿Deseas volver a jugar?:").lower()
    if again == "si":
        continue
    elif again == "no":
        print("Saliste del juego, vuelve pronto.")
        print("👻 Gracias por jugar.")
        exit()
    else:
        print("❌ Esta opción no es válida, vuelve a tratar.\n")