# Práctica 04: Torneo de los 3 Magos
# Author: Alejandro del Valle Vallés

from models.Campeon import Campeon
from models.Dragon import Dragon
from service.ReglasToreno import ReglasTorneo


def main():
    print("--- INICIO DEL TORNEO ---")

    harry = Campeon("Harry Potter", vida=100, energia=80, casa="Gryffindor")
    cedric = Campeon("Cedric Diggory", vida=100, energia=80, casa="Hufflepuff")
    colacuerno = Dragon("Colacuerno Húngaro", 300, tipo_fuego="Negro")

    harry.aprender_hechizo("Expelliarmus")
    harry.aprender_hechizo("Expecto Patronum")

    print(f"Harry conoce {len(harry)} hechizos.")
    print(f"Hay {Dragon.get_dragones_arena()} dragones en la arena.")

    if harry == cedric:
        print("Harry y Cedric están en condiciones idénticas al inicio.")
    else:
        print("Están en condiciones diferentes.")

    print("\n--- COMIENZA EL DUELO ---")
    harry.atacar(colacuerno)
    colacuerno.atacar(harry)

    print("\n--- INTENTO DE TRAMPA ---")
    harry.vida = -500

    print("\n--- ESTADO FINAL ---")
    print(harry)
    print(colacuerno)

    

if __name__ == '__main__':
    main()