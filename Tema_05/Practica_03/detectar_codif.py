import chardet
import sys
import os

def detectar_codificacion(ruta) -> str:
    with open(ruta, "rb") as f:
        data = f.read()
    resultado = chardet.detect(data)
    return resultado["encoding"]