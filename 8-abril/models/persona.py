class Persona:
    tipo = "Ser Humano"
    
    def _init_(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return self.nombre
    
    def saludar(self, persona_a_saludar):
        print(f"Hola, soy {self.nombre}, me da gusto conocerte {persona_a_saludar}")
        
     
print(__name__)        
if __name__ == "models.persona":
    print("Conectando a la API")
        

