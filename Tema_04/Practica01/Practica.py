# Alejandro del Valle Vallés
import elecciones_p1

def main():
    print(f"{elecciones_p1.SumaVotos(elecciones_p1.almeria)} Votos")
    print(f"El porcentaje del PP es de: ", elecciones_p1.PorcentajePartido(elecciones_p1.almeria, "PP"), "%")
    print(f"¿Hay aprtidos por debajo del 3% de votos? {elecciones_p1.HayPartidoExcluido(elecciones_p1.almeria)}")
    print(f"Los porcentajes por partido son: {elecciones_p1.PorcentajeEscrutinio(elecciones_p1.almeria)}")
    print(f"Exculyendo los partidos con menos del 3%, el resultado es: {elecciones_p1.ExclusionPequenos(elecciones_p1.almeria)}")

if __name__ == '__main__':
    main()