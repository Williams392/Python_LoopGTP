anals_nota = []
poo_notas = []
estructura_notas = []
promedios = {}

def ingresar_regist():
    id = input("ID: ")
    nombre = input("Nombre: ")
    notaFinal = float(input("Nota final: "))
    curso = int(input("Curso (1: Análisis de algoritmos, 2: POO, 3: Estructura de datos): "))
    if curso == 1:
        anals_nota.append(notaFinal)
    elif curso == 2:
        poo_notas.append(notaFinal)
    elif curso == 3:
        estructura_notas.append(notaFinal)
    return {"id": id, "nombre": nombre, "nota_final": notaFinal, "curso": curso}


def ingresar_regists(n):
    registros = []
    for i in range(n):
        print()
        print(f"Ingrese los datos del estudiante {i+1}:")
        # llamando la funcion ingresar_regist.
        registro = ingresar_regist()
        registros.append(registro)
    return registros


def calcular_promedio(curso_notas):
    if len(curso_notas) > 0:
        return sum(curso_notas) / len(curso_notas)
    else:
        return 0


n = int(input("Ingrese el número de registros: "))


registros = ingresar_regists(n)

analisis_promd = calcular_promedio(anals_nota)
poo_promd = calcular_promedio(poo_notas)
estructura_promd = calcular_promedio(estructura_notas)

promedios = {1: analisis_promd, 2: poo_promd, 3: estructura_promd}

# desempaquetado de tupla -> devolver como una lista.
print("Notas promedio por curso:")
for curso, promedio in promedios.items():
    #segun curso:
    print(f"Curso {curso}: {promedio}")

