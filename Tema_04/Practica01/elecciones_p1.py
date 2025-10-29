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

def suma_votos(escrutinio: tuple) -> int:
    """
    Deuvuelve la suma de todos los votos emitidos en una provincia.
    """
    return sum(votos for _, votos in escrutinio[2])

def procetnaje_partido(escrutinio: tuple, partido: str) -> float:
    """
    Devuelve el porcentaje de votos de un partido en una provincia.
    """
    total_votos_partido = next((votos for p, votos in escrutinio[2] if p == partido), 0)
    total_votos = suma_votos(escrutinio)
    
    if total_votos == 0:
        return 0.0
        
    return (total_votos_partido / total_votos) * 100.0

def hay_partido_excluido(escrutinio: tuple) -> bool:
    """
    Devuelve si hay algun partido exclusido con menos de un 3% de votos.
    """
    return any(porcentaje < 3.0 for _, porcentaje in porcentaje_escrutino(escrutinio))

def porcentaje_escrutino(escrutinio: tuple) -> list:
    """
    Devuelve una lista con el porcentaje de votos de cada partido.
    """
    return [(item[0], procetnaje_partido(escrutinio, item[0])) for item in escrutinio[2]]

def exclusion_pequenos(escrutinio: tuple) -> list:
    """
    Devuelve una lista donde no aparecen los partidos excluidos (Menos del 3% de votoso)
    """
    return [item for item in porcentaje_escrutino(escrutinio) if item[1] >= 3.0]
        

def partidos_no_considerados(escrutinio: tuple) -> list:
    return [item for item in porcentaje_escrutino(escrutinio) if item[1] < 3.0]

def partidos_considerados(escrutinio: tuple) -> list:
    return [partido for partido, escanos in repartir_escanos(escrutinio)]

def genera_patron(escrutinio: tuple) -> list:
    return porcentaje_escrutino(escrutinio)

def mas_nums_votos(partido_uno: str, partido_dos: str, escrutinio: tuple) -> str:
    votos: list = [0, 0]
    mas_votos: str = partido_dos
    
    for partido in escrutinio[2]:
        if partido[0] == partido_uno:
            votos[0] = partido[1] 
        elif partido[0] == partido_dos:
            votos[1] = partido[1]
        
    if votos[0] > votos[1]:
        mas_votos = partido_uno
    
    return mas_votos

def dame_coeficientes(escrutinio: tuple) -> list:
    """
    Recibe un escrutinio y devuelve una lista de (Partido, [Coeficientes]) 
    para los partidos que superan la barrera electoral (3%).
    """
    _, total_escanos, _ = escrutinio
    partidos_considerados = exclusion_pequenos(escrutinio)
    votos_elegibles = {}
    nombres_partidos_elegibles = [p[0] for p in partidos_considerados]
    
    for nombre, votos in escrutinio[2]:
        if nombre in nombres_partidos_elegibles:
            votos_elegibles[nombre] = votos

    lista_final_coeficientes = []
    
    for partido, votos in votos_elegibles.items():
        coeficientes_partido = []
        for divisor in range(1, total_escanos + 1):
            coeficientes_partido.append(votos / divisor)
        lista_final_coeficientes.append((partido, coeficientes_partido))
            
    return lista_final_coeficientes

def repartir_escanos(escrutinio: tuple) -> list:
    """
    Recibe un escrutinio y devuelve la asignación de escaños de TODOS 
    los partidos considerados (que superaron el 3%), incluso si obtienen 0 escaños.
    """
    _, total_escanos_distribuit, resultado_partido = escrutinio
    
    total_votos_validos = suma_votos(escrutinio)
    
    if total_votos_validos == 0 or total_escanos_distribuit == 0:
        return []

    min_votos_requeridos = total_votos_validos * 0.03

    partidos_elegibles = []
    for partido, votos in resultado_partido:
        if votos >= min_votos_requeridos:
            partidos_elegibles.append((partido, votos))

    if not partidos_elegibles:
        return []

    dhondt_tabla = []
    for partido, votos in partidos_elegibles:
        dhondt_tabla.append([partido, votos, 1, 0])

    for _ in range(total_escanos_distribuit):
        cociente_mas_alto = -1
        indice_partido_ganador = -1

        for i in range(len(dhondt_tabla)):
            datos_partido = dhondt_tabla[i]
            votos = datos_partido[1]
            divisor = datos_partido[2]
            
            cociente = votos / divisor
            
            if cociente > cociente_mas_alto:
                cociente_mas_alto = cociente
                indice_partido_ganador = i
            elif cociente == cociente_mas_alto:
                if dhondt_tabla[i][1] > dhondt_tabla[indice_partido_ganador][1]:
                    indice_partido_ganador = i

        if indice_partido_ganador != -1:
            dhondt_tabla[indice_partido_ganador][3] += 1
            dhondt_tabla[indice_partido_ganador][2] += 1
            
    final_esacanos_repartidos = []
    for partido, _, _, escanos_ganados in dhondt_tabla:
        final_esacanos_repartidos.append((partido, escanos_ganados))
            
    return final_esacanos_repartidos