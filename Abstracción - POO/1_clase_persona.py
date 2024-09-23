class Persona:
    __idea = ""

    def __init__(self, nombre, edad, cedula, pasaporte="", estudia=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__cedula = cedula
        self.__pasaporte = pasaporte
        self.__estudia = estudia

    def get_nombre(self):
        return print(f"nombre: {self.__nombre}")

    def set_nombre(self, nombre):
        self.__nombre = nombre
        return self.get_nombre()

    def get_edad(self):
        return print(f"edad: {self.__edad}")

    def set_edad(self, edad):
        self.__edad = edad
        return self.get_edad()

    def get_cedula(self):
        return print(f"Número de cedula: {self.__cedula}")

    def set_cedula(self, cedula):
        self.__cedula = cedula
        return self.get_cedula()

    def get_pasaporte(self):
        return print(f"Número de pasaporte: {self.__pasaporte}")

    def set_pasaporte(self, pasaporte):
        self.__pasaporte = pasaporte
        return self.get_pasaporte()

    def get_estudia(self):
        return print(f"estudia: {self.__estudia}")

    def set_estudia(self, estudia):
        self.__estudia = estudia
        return self.get_estudia()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    # Método privado para calcular la edad en meses
    def __calcular_edad_meses(self):
        return self.__edad * 12

    # Método privado para validar el nombre
    def __validar_nombre(self):
        if len(self.__nombre) < 3:
            return "El nombre es demasiado corto"
        return "El nombre es apropiado"

    # Método privado para actualizar la edad (simulando un cumpleaños)
    def __incrementar_edad(self):
        self.__edad += 1
        return f"Se incrementó la edad a: {self.__edad}"

    # Método privado para cambiar el género si es necesario
    def __cambiar_idea(self, idea):
        self.__idea = idea
        return f"Su nueva idea es: {self.__idea}"

    def metodo_publico(self, idea="Nueva Idea"):
        return print(
            f"{self.__metodo_privado()} \n {self.__calcular_edad_meses()} \n {self.__validar_nombre()} \n {self.__incrementar_edad()} \n {self.__cambiar_idea(idea)}"
        )

    def mostrar(self):
        print(
            f"Los datos de las persona {self.__nombre} son: \n Edad: {self.__edad} \n Cedula: {self.__cedula}"
        )

    def es_mayor_de_edad(self):
        if self.__edad < 18:
            print(f"La persona {self.__nombre} NO es mayor de edad")
        else:
            print(f"La persona {self.__nombre} SI es mayor de edad")


sebastian = Persona("Sebastian", 18, 29084699635)

sebastian.mostrar()
sebastian.es_mayor_de_edad()

sebastian.get_nombre()
sebastian.set_nombre("Jhon")

sebastian.get_edad()
sebastian.set_edad(19)

sebastian.get_cedula()
sebastian.set_cedula(3404730712)

sebastian.get_pasaporte()
sebastian.set_pasaporte("314235HU86")

sebastian.get_estudia()
sebastian.set_estudia(True)

sebastian.metodo_publico(idea="Fin del programa")
