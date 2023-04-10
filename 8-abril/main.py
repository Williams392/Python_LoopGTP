from models.persona import Persona

print("Llamando el archivo main")

if __name__ == "__main__":
    estudiante = Persona(nombre = "Jhon", apellido = "Doe", edad = 21)
    profesor = Persona(nombre = "wesley", apellido = "Smitch", edad = 31)
    
    estudiante.saludar(profesor)
    profesor.saludar(estudiante)



# estudiante = Persona(nombre = "Jhon", apellido = "Dextre", edad = 21)
# profesor = Persona(nombre = "wesley", apellido = "Smith", edad = 32)

# estudiante.saludar(profesor)