class Persona():
    def _init_(self):
        self.nombre = ""
        self.edad = 0
        self.dni = 0
        
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def getNombre(self):
        return self.nombre
    
    def setEdad(self, edad):
        if(edad >= 0):
            self.edad = edad
        else:
            # Mensaje de error si se ingresa una edad negativa
            print("Ha ingresado los datos incorrectamente")
            
    def getEdad(self):
        return self.edad
    
    def setDni(self, dni):
        self.dni = dni
        
    def getDni(self):
        return self.dni

# Instanciando a una persona
persona1 = Persona()

# Establecimiento de los atributos de la persona
persona1.setNombre("Jesus")
persona1.setEdad(18)
persona1.setDni("31200562")

# Impresión de los atributos de la persona
print(persona1.getNombre())
print(persona1.getEdad())
print(persona1.getDni())
