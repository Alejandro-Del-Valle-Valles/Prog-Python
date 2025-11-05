"""
Crear una función al que se le pase un número y un estilo de impresión por parámetro
y en base a eso generar una pirámide o una escalera con aumentando de 1 hasta el numero indicado.
"""
def piramide(numero: int):
    numeros: list = []
    for n in range(numero):
        numeros.append(n)
        print(" "*(numero - n),*numeros)

def escalera(numero: int):
    numeros: list = []
    for numero in range(numero):
        numeros.append(numero)
        print(*numeros)

def escalera_invertida(numero: int):
    numeros = []
    ancho = len(" ".join(str(i) for i in range(numero))) #Ancho de la última línea
    for i in range(numero):
        numeros.append(i)
        linea = " ".join(str(n) for n in numeros)
        print(linea.rjust(ancho))
        

def estructura(numero: int, posicion: int):
    match posicion:
        case 0:
            piramide(numero)
        case 1:
            escalera(numero)
        case 2:
            escalera_invertida(numero)
        case _:
            print("Posición no válida.")

def main():
    estructura(5, 2)

if __name__ == '__main__':
    main()