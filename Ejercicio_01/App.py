from Service import MenuService
from Service import AskDataService
from Service import PersonService
from Service import TravelService
import traceback


def main():
    user_input = None
    while True:
        try:
            MenuService.show_menu()
            user_input = AskDataService.ask_Int()
            execute_Options(user_input)
            if user_input == 0: break
        except Exception as e:
            print(f"Ha ocurrido un error inesperado.")
            traceback.print_exc()
            
def execute_Options(option: int):
    match option:
        case 0:
            print("Saliendo del programa...")
        case 1:
            PersonService.registration()
        case 2:
            TravelService.ask_To_Travel()

if __name__ == '__main__':
    main()