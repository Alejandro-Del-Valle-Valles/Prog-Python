
__DEFAULT_QUESTION = "Introduce una opción: "

def ask_String(question: str = __DEFAULT_QUESTION, allow_empty = False) -> str:
    user_input = None
    while True:
        print(question if isinstance(question, str) else "Introduce un texto:")
        user_input = input()
        
        if allow_empty or user_input != "":
            break
    
    return user_input
        
def ask_Int(question: str = __DEFAULT_QUESTION, is_Positive = True) -> int:
    user_input = None
    while True:
        try:
            print(question if isinstance(question, str) else "Introduce un texto:")
            user_input = int(input())
            
            if is_Positive and user_input >= 0: break
            elif not is_Positive: break
            else: print("El número debe ser positivo.")
        except:
            print("Debes introducir un valor numérico")
    
    return user_input
        
    
        