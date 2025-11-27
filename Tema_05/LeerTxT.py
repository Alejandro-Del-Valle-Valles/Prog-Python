from pathlib import Path
import time

def main():
    start: float = time.perf_counter()
    num_txt: int = sum(1 for file in Path.home().rglob("*.txt"))
    print(f"Numero total de ficheros .txt en el usuario: {num_txt}")
    print(f"Timpo total de ejecución: {(time.perf_counter() - start):.2f} segundos.")

if __name__ == '__main__':
    main()