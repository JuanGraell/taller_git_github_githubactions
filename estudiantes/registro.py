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
    """Ordena alfabéticamente e imprime una tabla con columnas alineadas."""
    if not estudiantes:
        print("No hay estudiantes para mostrar.")
        return

    # Ordenar por nombre
    lista = sorted(estudiantes, key=lambda e: e.nombre)

    # Calcular ancho de columnas
    ancho_nombre = max(len(e.nombre) for e in lista) + 2
    ancho_nota   = 6  # para mostrar e.g. "5.00"

    # Encabezado
    print(f"{'Nombre'.ljust(ancho_nombre)}| {'Nota'.rjust(ancho_nota)}")
    print("-" * (ancho_nombre + 3 + ancho_nota))

    # Filas
    for e in lista:
        print(f"{e.nombre.ljust(ancho_nombre)}| {e.nota:>.2f}".rjust(ancho_nota + ancho_nombre + 2))

def calcular_promedio(estudiantes):
    """Calcula y devuelve el promedio de notas con dos decimales."""
    if not estudiantes:
        return 0.0
    total = sum(e.nota for e in estudiantes)
    promedio = total / len(estudiantes)
    return round(promedio, 2)

def mostrar_promedio(promedio):
    """Imprime el promedio de notas."""
    print(f"\nPromedio general de notas: {promedio:.2f}")