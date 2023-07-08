"""
una nueva solución para abordar este problema usando recursión y backtracking. 
En este enfoque, vamos a generar todas las posibles asignaciones de forma 
sistemática y luego verificar si cada una de ellas cumple con las 
restricciones dadas.

"""

import itertools

# Definir los módulos y las materias con el número de clases correspondientes
modulos = [
    {'nombre': 'Módulo I', 'materias': ['A', 'B', 'C', 'K'], 'clases': [3, 1]},
    {'nombre': 'Módulo II', 'materias': ['D', 'E', 'F', 'G'], 'clases': [3, 2]},
    {'nombre': 'Módulo III', 'materias': ['H', 'I', 'J', 'L', 'M', 'N', 'O'], 'clases': [2, 1]}
]

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

    for modulo in modulos:
        materias_asignadas = [materia for materia in asignacion if materia in modulo['materias']]
        if len(materias_asignadas) != len(set(materias_asignadas)):
            return False

    return True

# Función para generar todas las posibles asignaciones de horarios
def generar_asignaciones(asignacion_actual, dias_restantes, horarios_restantes):
    if not dias_restantes:
        if verificar_restricciones(asignacion_actual):
            return [asignacion_actual]
        else:
            return []

    dia_actual = dias_restantes[0]
    posibles_asignaciones = []
    for horario in horarios_restantes:
        nueva_asignacion = asignacion_actual.copy()
        nueva_asignacion[dia_actual] = horario
        posibles_asignaciones.extend(generar_asignaciones(nueva_asignacion, dias_restantes[1:], horarios_restantes))

    return posibles_asignaciones

# Generar todas las posibles combinaciones de horarios
combinaciones_horarios = list(itertools.product(dias_semana, horarios))

# Generar todas las posibles asignaciones de horarios
posibles_asignaciones = generar_asignaciones({}, dias_semana, combinaciones_horarios)

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


