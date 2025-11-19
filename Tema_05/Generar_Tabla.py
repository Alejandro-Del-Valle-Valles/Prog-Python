
def preguntar_Numero() -> int:
    numero: int
    while True: 
        try:
            numero = int(input("Introduce un número: "))
            break
        except:
            print("Debes introducir un número.")
            
    return numero

def main():
    numero = preguntar_Numero()
    try :
        with open(f"tabla-{numero}.txt", encoding="utf-8", mode ="w") as f:
            for i in range(1, 11):
                print(f"{i} X {numero} = {i * numero}", file=f)
    except:
        print("Ha ocurrido un error al tratar de crear el fichero.")

if __name__ == '__main__':
    main()