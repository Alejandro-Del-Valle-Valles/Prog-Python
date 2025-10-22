from Menu import *

def main():
    option = -1
    while option != 0:
        Menu.show_menu()
        option = Menu.ask_Option()
        Menu.execute_menu_options(option)

if __name__ == '__main__':
    main()