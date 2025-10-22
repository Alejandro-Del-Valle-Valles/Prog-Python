import random
import os
import time

# Constants
TREE: str = "🌳"
FINISH_LINE: str = "🏁"
CAR_ONE: str = "🚗"
CAR_TWO: str = "🚙"
PATH: str = "_"

def clear_console():
    """Clears the console screen (works on Windows, macOS, and Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_circuit_length() -> int:
    """
    Asks the user for the circuit length until a valid number (greater than 3) is entered.
    
    Returns:
        int: The desired length for the circuit's path.
    """
    length: int
    while True:
        try:
            print("Introduce la longitud que quieres que tenga la pista:")
            length_input = input()
            length = int(length_input)
            
            if length > 3:
                break
            else:
                print("La longitud debe ser positiva y superior a 3.")
        except ValueError: 
            print("Debes introducir un número entero positivo.")
    return length

def start_race():
    """Waits for user input and clears the console to start."""
    print("Presiona enter para empezar la carrera...")
    input()
    clear_console() 

def generate_circuit(length: int, car: str) -> str:
    """
    Generates a circuit string with 1-3 trees.
    
    Args:
        length (int): The length of the path (between finish and start).
        car (str): The car emoji to place at the start.

    Returns:
        str: The complete circuit string (e.g., "🏁___🌳_🚗")
    """
    char_list = [PATH] * length
    nums_of_trees = random.randint(1, 3)
    placed_trees_count = 0
    
    while placed_trees_count < nums_of_trees:
        random_index = random.randint(0, length - 1)
        if char_list[random_index] == PATH:
            char_list[random_index] = TREE
            placed_trees_count += 1
            
    return FINISH_LINE + "".join(char_list) + car

def run_race(circuit_one_str: str, circuit_two_str: str):
    """
    Main loop for running the race.
    
    Args:
        circuit_one_str (str): The initial string for player one's circuit.
        circuit_two_str (str): The initial string for player two's circuit.
    """
    winner: str = ""
    player_one_circuit = list(circuit_one_str)
    player_two_circuit = list(circuit_two_str)
    
    random_one: int
    random_two: int

    while True:
        one_won = check_winner(player_one_circuit, CAR_ONE)
        two_won = check_winner(player_two_circuit, CAR_TWO)
        
        if one_won and two_won:
            winner = "Empate"
            break
        elif one_won:
            winner = "Jugador Uno"
            break
        elif two_won:
            winner = "Jugador Dos"
            break

        clear_console()
        print("".join(player_one_circuit))
        print("".join(player_two_circuit))

        random_one = random.randint(1, 3)
        random_two = random.randint(1, 3)

        time.sleep(1)

        update_circuit(player_one_circuit, random_one, CAR_ONE)
        update_circuit(player_two_circuit, random_two, CAR_TWO)

    clear_console()
    print("".join(player_one_circuit))
    print("".join(player_two_circuit))
    print(f"\n¡La carrera ha terminado!")
    print(f"El ganador es: {winner}")


def update_circuit(circuit: list[str], moves: int, car: str):
    """
    Updates the circuit list by moving the car forward (left).
    The list is modified "in-place" (directly).

    Args:
        circuit (list[str]): The circuit list to modify.
        moves (int): The number of steps to attempt to move.
        car (str): The car string to move.
    """
    try:
        current_pos = circuit.index(car)
    except ValueError:
        return
    
    for _ in range(moves):
        next_pos = current_pos - 1 
        if next_pos < 0:
            break
            
        destination = circuit[next_pos]

        if destination == FINISH_LINE:
            circuit[next_pos] = car
            circuit[current_pos] = PATH
        elif destination == TREE:
            circuit[next_pos] = car
            circuit[current_pos] = PATH
            break
        elif destination == PATH:
            circuit[next_pos] = car
            circuit[current_pos] = PATH
            current_pos = next_pos
        else:
            break 


def check_winner(circuit: list[str], car: str) -> bool:
    """
    Checks if the car has reached the finish line (index 0).
    
    Args:
        circuit (list[str]): The circuit list.
        car (str): The car to check.

    Returns:
        bool: True if the car is at index 0, False otherwise.
    """
    return circuit[0] == car

def main():
    """Main function to run the application."""
    length = ask_circuit_length()
    circuit_one = generate_circuit(length, CAR_ONE)
    circuit_two = generate_circuit(length, CAR_TWO)
    
    start_race()
    run_race(circuit_one, circuit_two)

if __name__ == "__main__":
    main()