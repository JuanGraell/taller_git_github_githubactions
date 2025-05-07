from estudiantes.registro import cargar_estudiantes, mostrar_tabla, calcular_promedio, mostrar_promedio

def main():
    ruta = "estudiantes.csv"
    estudiantes = cargar_estudiantes(ruta)
    mostrar_tabla(estudiantes)
    promedio = calcular_promedio(estudiantes)
    mostrar_promedio(promedio)

if __name__ == "__main__":
    main()
