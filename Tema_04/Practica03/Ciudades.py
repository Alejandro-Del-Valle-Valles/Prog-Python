'''
Alejandro del Valle Vallés
=========
Ejercicio 3: Calcular opciones y tiempo desde Madrid a otras ciudades.
Si la distancia es menor que 50, velocidad máxima 90 km/h.
Si está entre 50 y 300, 120 km/h.
Si está entre 300 y 1000, 500 km/h + 1 hora
Si es superior a 1000, 900km/h + 3 horas
'''
NEAR_CITIES_KM: int = 90
MEDIUM_CITIES_KM: int = 120
LARGE_DISTANCE_KM: int = 500
INTERNATIONAL_CITIES_KM: int = 900


def get_Cities() -> dict:
    """Diccionario de ciudades con sus respectivas distancias desde Madrid

    Returns:
        dict: str, int
    """
    return {"Guadalajara": 66, "Toledo": 72, "Segovia": 91, "Ávila": 109, "Cuenca": 171,
            "Zaragoza": 320, "Valencia": 361, "Pampolna": 391, "Bilbao": 404, "Alicante": 426,
            "Málaga": 535, "A Coruña": 592, "Barcelona": 627, "Cádiz": 647, "Sevilla": 531,
            "París": 1280, "Londres": 1733, "Roma": 1966, "Bruselas": 1629, "Berlín": 2328}
        
def ask_City() -> str:
    """Muestra y pregunta al usuario para que elija una ciudad a la que viajar.

    Returns:
        str: Devuelve la ciudad seleccionada.
    """
    city: str
    while True:
        for k in get_Cities(): print(k, end=" | ")
        print()
        print("Introduce la ciudad a la que quieres viajar: ")
        city = input().strip().capitalize()
        if city in get_Cities():
            break
        
    return city

def calculate_Distance_Time(city: str) -> float:
    """Calcula el timpo que se va a tardar hasta la ciudad seleccionada.
    La velocidad a la que puede viajar varía de la distancia a la ciudad.
    Args:
        city (str): Ciudad a la que quiere viajar

    Returns:
        float: tiempo que se tarda en viajar.
    """
    distance = get_Cities()[city]
    match distance:
        case distance if distance < 50:
            return distance / NEAR_CITIES_KM
        case distance if 50 <= distance < 300:
            return distance / MEDIUM_CITIES_KM
        case distance if 300 <= distance < 1000:
            return (distance / LARGE_DISTANCE_KM) + 1 #Se añade una hora
        case distance if 1000 <= distance:
            return (distance / INTERNATIONAL_CITIES_KM) + 3 #Se añaden 3 horas
        case _:
            print(f"No se ha encontrado distancia para la ciudad {city}.")
            return 0

def main():
    city: str = ask_City()
    print(f"Para viajar a {city} vas a tardar {calculate_Distance_Time(city):.2f} horas")
    print(f"La distancia entre ambas ciudades es de {get_Cities()[city]}Km.")

if __name__ == '__main__':
    try:
        main()
    except:
        print("Ha ocurrido un error inesperado.")
    