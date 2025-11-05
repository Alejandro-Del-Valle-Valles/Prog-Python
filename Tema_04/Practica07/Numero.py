# Normalizar los número de teléfono quitando todo lo que no sean números. Cambiar los + por 00.
# Crear un diccionario agrupando por el prefijo, si es 00 se cogeran 4 núero (ej 0036),
# si no es 00 pues los 2 primeros numeros.

import re #Lo hice con expresión regular

lista_numeros: list = ["+3074974928", "627726661", "(0036)712-991",
                       "680 250 312"]

def normalizar_numeros() -> list:
    lista = [numero.replace("+", "00").strip() for numero in lista_numeros]
    return [re.sub(r"\D", "", numero) for numero in lista]

def crear_diccionario(lista: list) -> dict:
    diccionario = {}
    for numero in lista:
        if numero[:2] == "00":
            if numero[:4] not in diccionario:
                diccionario[numero[:4]] = [numero[4::]]
            else:
                diccionario[numero[:4]].append(numero[4::])
        else:
            if numero[:2] not in diccionario:
                diccionario[numero[:2]] = [numero[2::]]
            else:
                diccionario[numero[:2]].append(numero[2::])
    return diccionario

def main():
    print(crear_diccionario(normalizar_numeros()))

if __name__ == '__main__':
    main()