'''
El ejercicio consiste en analizar un array de 'bolas' marcadas por cada jugador.
La función tiene que contar el orden en el que aparecen e ir sumando los puntos.
Cuando un jugador supere la 'ventaja' y el otro jugador no esté en el mismo puntaje, ganará, si no, hasta que
uno de los dos sace dos puntos más que el otro, el partido sigue.
'''
p1: str = "P1"
p2: str = "P2"
points: list[str]= [p1, p1, p2, p1, p2, p2, p2, p1, p2, p1, p2, p1, p2, p2]

def check_points() -> str:
    points_one: int = 0
    points_two: int = 0
    one_win: bool
    two_win: bool
    for point in points:
        if point == p1:
            points_one += 1
        else:
            points_two += 1
        one_win = check_winner(points_one, points_two)
        two_win = check_winner(points_two, points_one)
        if one_win:
            return "Jugador 1"
        elif two_win:
            return "Jugador 2"
            
def check_winner(points_one: int, points_two: int) -> bool:
    if points_one == 5 and points_two < 4:
        return True
    elif points_one > 5 and points_one - 2 == points_two:
        return True
    else:
        return False

def main():
    print(check_points())

if __name__ == '__main__':
    main()