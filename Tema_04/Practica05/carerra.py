import random

tree: str = "🌳"
finish_line: str = "🏁"
car_one: str = "🚗"
car_two: str = "🚙"
cirucit_one: str = ""
cirucit_two: str = ""

def ask_circuit_length() -> int:
    length: int
    while True:
        try:
            print("Introduce la longitud que quieres que tenga la pista:")
            length = int(input())
            if length > 3:
                break
            else:
                print("La longitud debe ser positiva y superior a 3.")  
        except:
            print("Debes introducir un número entero positivo")
    return length

def generate_circuit(length: int, car: str) -> str:
    circuit = "_" * length
    char_list = list(circuit)
    nums_of_threes = random.randint(1, 3)
    for i in range(0, nums_of_threes):
        random_index = random.randint(0, len(char_list))
        if char_list[random_index] != tree:
            char_list[random_index] = tree
    return finish_line + "".join(char_list) + car

def main():
    length = ask_circuit_length()
    cirucit_one = generate_circuit(length,car_one)
    cirucit_two = generate_circuit(length, car_two)
    print(cirucit_one)
    print(cirucit_two)

if __name__ == "__main__":
    main()