class Persona():
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        
    def mostrar(self):
        print(f"Los datos de las persona {self.nombre} son: \n Edad: {self.edad} \n Cedula: {self.cedula}")
        
    def es_mayor_de_edad(self):
        if self.edad < 18:
            print(f"La persona {self.nombre} NO es mayor de edad")
        else:
            print(f"La persona {self.nombre} SI es mayor de edad")
        
        
sebastian = Persona("Sebastian", 18, 29084699635)

sebastian.mostrar()
sebastian.es_mayor_de_edad()