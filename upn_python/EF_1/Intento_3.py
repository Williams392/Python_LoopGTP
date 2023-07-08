"""
una nueva solución para abordar este problema usando recursión y backtracking. 
En este enfoque, vamos a generar todas las posibles asignaciones de forma 
sistemática y luego verificar si cada una de ellas cumple con las 
restricciones dadas.

"""

# Definir las materias con el número de clases correspondientes
materias = {
    'A': 3, 'B': 3, 'C': 3, 'K': 1,
    'D': 3, 'E': 3, 'F': 3, 'G': 2,
    'H': 2, 'I': 2, 'J': 2, 'L': 1,
    'M': 1, 'N': 1, 'O': 1
}

# Definir los días de la semana y los horarios disponibles
dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
horarios = ['horario1', 'horario2', 'horario3']

# Función para verificar si una asignación cumple con las restricciones
def verificar_restricciones(asignacion):
    for dia, horario in asignacion.items():
        clases_dia = [materia for materia, hora in asignacion.items() if hora == horario]
        if len(clases_dia) > 2:
            return False

        materias_dia = [materia for materia, hora in asignacion.items() if hora[0] == dia[0]]
        if len(materias_dia) != len(set(materias_dia)):
            return False

    return True

# Función de backtracking para generar las asignaciones válidas
def generar_asignaciones(asignacion_actual, indice_materia):
    if indice_materia == len(materias):
        if verificar_restricciones(asignacion_actual):
            return [asignacion_actual]
        else:
            return []

    materia = list(materias.keys())[indice_materia]
    posibles_asignaciones = []

    for dia in dias_semana:
        for horario in horarios:
            asignacion_actual[materia] = (dia, horario)

            if verificar_restricciones(asignacion_actual):
                posibles_asignaciones.extend(generar_asignaciones(asignacion_actual.copy(), indice_materia + 1))

            del asignacion_actual[materia]

    return posibles_asignaciones

# Generar todas las posibles asignaciones
posibles_asignaciones = generar_asignaciones({}, 0)

# Imprimir la solución encontrada
if posibles_asignaciones:
    print("Soluciones encontradas:")
    for i, asignacion in enumerate(posibles_asignaciones, 1):
        print(f"Solución {i}:")
        for dia, horario in asignacion.items():
            print(f"Materia: {dia}, Horario: {horario}")
        print()
else:
    print("No se encontró ninguna solución válida.")

