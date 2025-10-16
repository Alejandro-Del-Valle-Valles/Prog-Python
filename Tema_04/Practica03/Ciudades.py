'''
Ejercicio 3: Calcular opciones y tiempo desde Madrid a otras ciudades.
Si la distancia es menor que 50, velocidad máxima 90 km/h.
Si está entre 50 y 300, 120 km/h.
Si está entre 300 y 1000, 500 km/h + 1 hora
Si es superior a 1000, 900km/h + 3 horas
'''

def get_Cities() -> dict:
        return {"Guadalajara": 66, "Toledo": 72, "Segovia": 91, "Ávila": 109, "Cuenca": 171,
                "Zaragoza": 320, "Valencia": 361, "Pampolna": 391, "Bilbao": 404, "Alicante": 426,
                "Málaga": 535, "A Coruña": 592, "Barcelona": 627, "Cádiz": 647, "Sevilla": 531,
                "París": 1280, "Londres": 1733, "Roma": 1966, "Bruselas": 1629, "Berlín": 2328}

def main():
    pass

if __name__ == '__main__':
    main()