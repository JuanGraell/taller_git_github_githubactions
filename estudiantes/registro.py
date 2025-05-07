import csv
from collections import namedtuple

Estudiante = namedtuple("Estudiante", ["nombre", "nota"])

def cargar_estudiantes(ruta_csv):
    """Lee y valida estudiantes desde un CSV. 
    Sólo incluye notas entre 0.0 y 5.0."""
    estudiantes = []
    with open(ruta_csv, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            try:
                nota = float(fila["nota"])
                if 0.0 <= nota <= 5.0:
                    estudiantes.append(Estudiante(fila["nombre"], nota))
                else:
                    # Nota fuera de rango: ignorar o loggear
                    pass
            except (ValueError, KeyError):
                # Línea mal formada: ignorar o loggear
                pass
    return estudiantes

def mostrar_tabla(estudiantes):
    """Imprime los estudiantes en formato tabular."""
    pass

def calcular_promedio(estudiantes):
    """Calcula y devuelve el promedio de notas."""
    pass

def mostrar_promedio(promedio):
    """Imprime el promedio de notas."""
    pass