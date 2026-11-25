playlist = []

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Mostrar canciones")
    print("2. Actualizar populares")
    print("3. Eliminar canción")
    print("4. Buscar canción")
    print("5. Agregar canción")
    print("6. Salir")
    print("====================================")


def leer_opcion():
    opcion_valida = False

    while not opcion_valida:
        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion >= 1 and opcion <= 6:
                opcion_valida = True
            else:
                print("Error: ingrese un número entre 1 y 6.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    return opcion


def validar_nombre(nombre):
    if nombre.strip() != "" and len(nombre.strip()) >= 2:
        return True
    else:
        return False


def validar_minutos(minutos):
    if minutos >= 2:
        return True
    else:
        return False


def validar_descargas(descargas):
    if descargas > 0:
        return True
    else:
        return False


def actualizar_populares(lista):
    for cancion in lista:
        if cancion["descargas"] > 500:
            cancion["popular"] = True
        else:
            cancion["popular"] = False


def mostrar_canciones(lista):
    actualizar_populares(lista)

    if len(lista) == 0:
        print("La playlist está vacía.")
    else:
        for cancion in lista:
            print("\nNombre:", cancion["nombre"])
            print("Duración:", cancion["minutos"])
            print("Descargas:", cancion["descargas"])

            if cancion["popular"] == True:
                print("Estado: POPULAR")
            else:
                print("Estado: ESTÁNDAR")


def buscar_cancion(lista, nombre):
    posicion = -1

    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre:
            posicion = i
            break

    return posicion


def agregar_cancion(lista):
    nombre = input("Ingrese el nombre: ")

    if validar_nombre(nombre) == False:
        print("Nombre inválido.")
    else:
        try:
            minutos = int(input("Ingrese los minutos: "))

            if validar_minutos(minutos) == False:
                print("Los minutos deben ser mayores o iguales a 2.")
            else:
                try:
                    descargas = int(input("Ingrese las descargas: "))

                    if validar_descargas(descargas) == False:
                        print("Las descargas deben ser mayores a 0.")
                    else:
                        cancion = {
                            "nombre": nombre,
                            "minutos": minutos,
                            "descargas": descargas,
                            "popular": False
                        }

                        lista.append(cancion)
                        print("Canción agregada correctamente.")

                except ValueError:
                    print("Error: ingrese descargas enteras.")

        except ValueError:
            print("Error: ingrese minutos enteros.")


opcion = 0

while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        mostrar_canciones(playlist)

    elif opcion == 2:
        actualizar_populares(playlist)
        print("Populares actualizadas.")

    elif opcion == 3:
        nombre = input("Ingrese la canción que desea eliminar: ")
        posicion = buscar_cancion(playlist, nombre)

        if posicion != -1:
            playlist.pop(posicion)
            print("Canción eliminada.")
        else:
            print("La canción no se encuentra.")

    elif opcion == 4:
        nombre = input("Ingrese la canción que desea buscar: ")
        posicion = buscar_cancion(playlist, nombre)

        if posicion != -1:
            cancion = playlist[posicion]

            print("Posición:", posicion + 1)
            print("Nombre:", cancion["nombre"])
            print("Minutos:", cancion["minutos"])
            print("Descargas:", cancion["descargas"])
        else:
            print("Canción no encontrada.")

    elif opcion == 5:
        agregar_cancion(playlist)

    elif opcion == 6:
        print("Gracias por usar el gestor de playlist. ¡Hasta luego!")