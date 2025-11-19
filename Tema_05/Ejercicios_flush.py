import time
import itertools
"""
for i in range(10, 0, -1):
    print(f"\r{i}", end="", flush=True)
    time.sleep(0.5)
"""

""" 
for i in range(11):
    print(f"\rCargando [{'⬜' * i}{'..' * (10 - i)}]{i * 10}%", end="", flush=True)
    time.sleep(0.5)
"""
 
numero = int(input("Introduce un número: "))
puntos = itertools.cycle(['.', '..', '...'])
for i in range(10):
    print(f"\rCalculando {next(puntos)}      ", end="", flush=True)
    time.sleep(0.3)
    
print()
for i in range(11):
    print(f"{i} X {numero} = {i * numero}")