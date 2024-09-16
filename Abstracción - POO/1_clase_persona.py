class Persona:
    def __init__(self, nombre, edad, cedula, pasaporte=""):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.__pasaporte = pasaporte

    def get_pasaporte(self):
        return print(f"Número de pasaporte: {self.__pasaporte}")

    def set_pasaporte(self, pasaporte):
        self.__pasaporte = pasaporte
        return self.get_pasaporte()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

    def mostrar(self):
        print(
            f"Los datos de las persona {self.nombre} son: \n Edad: {self.edad} \n Cedula: {self.cedula}"
        )

    def es_mayor_de_edad(self):
        if self.edad < 18:
            print(f"La persona {self.nombre} NO es mayor de edad")
        else:
            print(f"La persona {self.nombre} SI es mayor de edad")


sebastian = Persona("Sebastian", 18, 29084699635)

sebastian.mostrar()
sebastian.es_mayor_de_edad()
sebastian.get_pasaporte()
sebastian.set_pasaporte("314235HU86")
sebastian.metodo_publico()
