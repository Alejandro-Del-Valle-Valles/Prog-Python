'''
Puntuación de la palabra: Consiste en pedir al usuario que introduzca 
palabras hasta que la puntuación de dicha palabra sea exacatmente de 100.
Cada letra tiene un valor que va de 1 con la A hasta 27 con la Z.
'''
import string
letras_peso = {
        letter: index 
        for index, letter in enumerate(string.ascii_lowercase.replace('o', 'ño'), 1)
    }

def preguntar() -> str:
    palabra: str
    while True:
        palabra = input("Introduce una palabra: ")
        if(palabra.strip() != ""):
            break
    return palabra

def calcular_puntuacion(palabra: str) -> int:
    puntuacion: int = 0
    for letra in palabra:
        puntuacion += letras_peso.get(letra.lower(), 0)
    return puntuacion

def main():
    while True:
        palabra = preguntar()
        puntuacion = calcular_puntuacion(palabra)
        print(f"Puntuación {puntuacion}")
        if(puntuacion == 100):
            break
        else:
            print("La palabra no da una puntuación exacta de 100")
    print("Has ganado")

if __name__ == '__main__':
    main()