#ANDALUCÍA
#Ejercicio de Alejandro del Valle Vallés

almeria = ("Almeria",  5, [("PP", 134328), ("PSOE", 115558), ("IU", 11742), ("PA", 6554),  ("Otros", 2871)])
   
cadiz   = ("Cadiz",    9, [("PP", 227315), ("PSOE", 216447), ("IU", 36662), ("PA", 54475), ("Otros", 9313)])
   
cordoba = ("Cordoba",  7, [("PP", 187955), ("PSOE", 185359), ("IU", 54713), ("PA", 20925), ("Otros", 3705)])
   
granada = ("Granada",  7, [("PP", 203569), ("PSOE", 209693), ("IU", 34483), ("PA", 16487), ("Otros", 4678)])
   
huelva  = ("Huelva",   5, [("PP", 98371),  ("PSOE", 114537), ("IU", 15668), ("PA", 11598), ("Otros", 1569)])
   
jaen    = ("Jaen",     6, [("PP", 160855), ("PSOE", 189901), ("IU", 28293), ("PA", 13020), ("Otros", 1896)])
   
malaga  = ("Malaga",  10, [("PP", 280854), ("PSOE", 250578), ("IU", 52354), ("PA", 33496)])
  
sevilla = ("Sevilla", 13, [("PP", 338908), ("PSOE", 473836), ("IU", 80154), ("PA", 49221)])

def SumaVotos(escrutinio: tuple) -> int:
    return sum(votos for _, votos in escrutinio[2])

def PorcentajePartido(escrutinio, partido) -> int:
    total_votos = SumaVotos(escrutinio)
    total_votos_partido = next((votos for p, votos in escrutinio[2] if p == partido), 0)
    return int((total_votos_partido / total_votos)*100)

def HayPartidoExcluido(escrutinio) -> bool:
    return any(porcentaje < 3 for _, porcentaje in PorcentajeEscrutinio(escrutinio))

def PorcentajeEscrutinio(escrutinio) -> list:
    return [(item[0], PorcentajePartido(escrutinio, item[0])) for item in escrutinio[2]]

def ExclusionPequenos(escrutinio):
    return [item for item in PorcentajeEscrutinio(escrutinio) if item[1] > 3]

