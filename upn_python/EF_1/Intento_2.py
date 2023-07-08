modulos = [
    {'nombre': 'Módulo I', 'materias': ['A', 'B', 'C', 'K'], 'clases': [3, 1]},
    {'nombre': 'Módulo II', 'materias': ['D', 'E', 'F', 'G'], 'clases': [3, 2]},
    {'nombre': 'Módulo III', 'materias': ['H', 'I', 'J', 'L', 'M', 'N', 'O'], 'clases': [2, 1]}
]

dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
horarios = ['horario1', 'horario2', 'horario3']

def verificar_restricciones(asignacion):
    for dia, horario in asignacion.items():
        clases_dia = [materia for materia, hora in asignacion.items() if hora == horario]
        if len(clases_dia) > 2:
            return False

        materias_dia = [materia for materia, hora in asignacion.items() if hora[0] == dia[0]]
        if len(materias_dia) != len(set(materias_dia)):
            return False

    for modulo in modulos:
        materias_asignadas = [materia for materia in asignacion if materia in modulo['materias']]
        if len(materias_asignadas) != len(set(materias_asignadas)):
            return False

    return True

def generar_asignaciones(asignacion_actual, indice_materia):
    if indice_materia == len(modulos):
        if verificar_restricciones(asignacion_actual):
            return [asignacion_actual]
        else:
            return []

    posibles_asignaciones = []
    for dia in dias_semana:
        for horario in horarios:
            asignacion_actual[dia] = (dia, horario)
            posibles_asignaciones.extend(generar_asignaciones(asignacion_actual.copy(), indice_materia + 1))
            del asignacion_actual[dia]

    return posibles_asignaciones


posibles_asignaciones = generar_asignaciones({}, 0)

# Imprimir la solución encontrada
if posibles_asignaciones:
    print("Soluciones encontradas:")
    for i, asignacion in enumerate(posibles_asignaciones, 1):
        print(f"Solución {i}:")
        for dia, horario in asignacion.items():
            print(f"Día: {dia}, Horario: {horario}")
        print()
else:
    print("No se encontró ninguna solución válida.")

