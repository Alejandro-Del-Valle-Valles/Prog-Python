import re
escrutino = ("alemría", 5, [("Paco", 542034), ("Po", 203), ("co", 54203), ("aco", 5434)])

print([(k, v) for k, v in escrutino[2] if re.match(r'p', k, re.IGNORECASE) and v % 2 == 0])
