'''
Ejercicio 2
Contador de letras o numeros y comprobación de si su número de apariciones es par o impar
'''
def count_and_Check_Even_Odd(text: str) -> dict:
    tuple_text: tuple = tuple(text.split(",")) #Partimos por comas para más tarde comprobar si son todo dígitos
    all_text_is_numeric = all(i.isdigit() for i in tuple_text) #Comprobamos si todo son digitos
    data: dict = {}
    if all_text_is_numeric:
        data: dict = {n: tuple_text.count(n) % 2 == 0 for n in tuple_text}
        #Por cada dígito le metemos como calve y su valor contamos el numero de apariciones
        #Y si el nº de apariciones es par, se le asigna True o False como valor.
    else:
        data = {char: text.replace(" ", "").count(char) % 2 == 0 for char in text.replace(" ", "")}
        #Por cada letra, usamos la letra como clave (Distingue mayúsculas de minusculas)
        #Y el valor es boolean si el nº de veces que aparece dicha letra es par o no.
    return data

def ask_String(message: str = "Introduce un texto: ") -> str:
    text_input: str
    while True:
        print(message)
        text_input = input().strip()
        if text_input == "" or text_input == None:
            print("Debes introducir un texto. No se permiten espacios en blanco.")
        else:
            break
    return text_input


def main():
    print(count_and_Check_Even_Odd(ask_String()))
    

if __name__ == '__main__':
    main()