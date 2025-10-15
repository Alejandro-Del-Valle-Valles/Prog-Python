'''
Ejercicio 1
Conversiones de un tipo de grado a otro.
'''

#First Option
def calculate_Kelvin_To_Celsius():
    kelvin: float = ask_Float_Number("Introduce la temperatura en Kelvin: ")
    celsius: float = kelvin - 273.15
    print(f"{kelvin:.2f}K a Cº: {celsius:.2f}")
    
#Second Option
def calculate_Celsius_To_Kelvin():
    celsius: float = ask_Float_Number("Introduce la temperatura en Cº: ")
    kelvin: float = celsius + 273.15
    print(f"{celsius:.2f}Cº a K: {kelvin:.2f}")
    
#Third Opion
def calculate_Kelvin_To_Fahrenheit():
    kelvin: float = ask_Float_Number("Introduce la temperatura en Kelvin: ")
    fahrenheit: float = ((kelvin - 273.15) * 9/5) + 32
    print(f"{kelvin:.2f}K a F: {fahrenheit:.2f}")

#Fourth Option
def calculate_Fahrenheit_To_Kelvin():
    fahrenheit: float = ask_Float_Number("Introduce la temperatura en Fahrenheit: ")
    kelvin: float = ((fahrenheit - 32) * 5/9) + 273.15
    print(f"{fahrenheit:.2f}F a K: {kelvin:.2f}")
    
#Fifth Option
def calculate_Celsius_To_Fahrenheit():
    celsius: float = ask_Float_Number("Introduce la temperatura en Cº: ")
    fahrenheit: float = (celsius * 9/5) + 32
    print(f"{celsius:.2f}Cº a F: {fahrenheit:.2f}")
    
#Sixth Option
def calculate_Fahrenheit_To_Celsius():
    fahrenheit: float = ask_Float_Number("Introduce la temperatura en Fahrenheit: ")
    celsius: float = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}F a Cº: {celsius:.2f}")

def ask_Int_Number(message: str = "Introduce una opción: ", isPositive = True) -> int:
    number_input: int
    while True:
        try:
            print(message)
            number_input = int(input())
            if isPositive and number_input < 0:
                print("El número debe ser positivo.")
                raise ValueError
            break
        except ValueError:
            print("Debes introducir un número entero.")
            
    return number_input

def ask_Float_Number(message: str = "Introduce una opción: ", isPositive = True) -> float:
    number_input: int
    while True:
        try:
            print(message)
            number_input = float(input())
            if isPositive and number_input < 0:
                print("El número debe ser positivo")
                raise ValueError
            break
        except ValueError:
            print("Debes introducir un número entero.")
            
    return number_input
    

def menu_Actions(option: int):
    match option:
        case 0:
            print("Saliendo del programa.")
        case 1:
            calculate_Kelvin_To_Celsius()
        case 2:
            calculate_Celsius_To_Kelvin()
        case 3:
            calculate_Kelvin_To_Fahrenheit()
        case 4:
            calculate_Fahrenheit_To_Kelvin()
        case 5:
            calculate_Celsius_To_Fahrenheit()
        case 6:
            calculate_Fahrenheit_To_Celsius()
        case _:
            print("Opción no válida.")
            
def show_Menu():
    options: tuple = ("Salir", "Kelvin a Celsius", "Celsius a Kelvin",
                      "Kelvin a Fahrenheit", "Fahrenheit a Kelvin", 
                      "Celsius a Fahrenheit", "Fahrenheit a Celsius")
    for i in range(len(options)):
        print(f"{i}. {options[i]}")

def main():
    option: int
    while True:
        show_Menu()
        option = ask_Int_Number()
        menu_Actions(option)
        if option == 0:
            break


if __name__ == '__main__':
    main()