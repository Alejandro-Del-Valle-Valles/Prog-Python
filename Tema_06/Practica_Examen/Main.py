#Ejercicio propuesto en clase

from Menu import Menu

def ejecutar_opcion(option: int):
    pass

def main():
    opcion = -1
    while opcion != 0:
        Menu.show_menu()
        opcion = int(input("Elige una opción: "))
        ejecutar_opcion(opcion)


if __name__ == '__main__':
    main()