class Persona:
    def __init__(self, nombre, edad, DNI, sexo, peso, altura, DIAN=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__DIAN = DIAN

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_DNI(self):
        return self.__DNI

    def set_DNI(self, DNI):
        self.__DNI = DNI

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_DIAN(self):
        return print(f"Declaración DIAN: {self.__DIAN}")

    def set_DIAN(self, DIAN):
        self.__DIAN = DIAN
        return self.get_DIAN()

    # Métodos privados
    def __validar_nombre(self):
        return f"Validando nombre: {self.__nombre}"

    def __validar_edad(self):
        return f"Validando edad: {self.__edad}"

    def __validar_DNI(self):
        return f"Validando DNI: {self.__DNI}"

    def __validar_sexo(self):
        return f"Validando sexo: {self.__sexo}"

    def __validar_peso(self):
        return f"Validando peso: {self.__peso}"

    # Método público que usa los métodos privados
    def metodo_publico(self):
        print(self.__validar_nombre())
        print(self.__validar_edad())
        print(self.__validar_DNI())
        print(self.__validar_sexo())
        print(self.__validar_peso())

    def calcularIMC(self):
        if self.__altura > 3:
            print("Por favor ingrese la altura en metros")
            return

        if self.__peso > 200:
            print("Por favor ingrese el peso en kilogramos")
            return

        peso_ideal = self.__peso / (self.__altura**2)

        if peso_ideal < 20:
            print("-1")
        elif 20 <= peso_ideal <= 25:
            print("Está por debajo de su peso ideal 0")
        else:
            print("Tiene sobrepeso 1")

    def esMayorDeEdad(self):
        if self.__edad < 18:
            return print(False)
        else:
            return print(True)

    def comprobarSexo(self, sexo):
        sexos = ["H", "M"]

        if sexo in sexos:
            if self.__sexo == sexo:
                print("El sexo es correcto")
            else:
                print(
                    f"El sexo es incorrecto, usted había ingresado previamente: {self.__sexo}"
                )
        else:
            print(
                f"Su valor ingresado ({sexo}) no es una opción del sistema. Las opciones del sistema son: {sexos}"
            )


persona_uno = Persona(
    nombre="Gabriel",
    edad=24,
    DNI=29650233528,
    sexo="H",
    peso=66,
    altura=1.76,
)

# Usando los getters
print(f"Nombre: {persona_uno.get_nombre()}")
print(f"Edad: {persona_uno.get_edad()}")
print(f"DNI: {persona_uno.get_DNI()}")
print(f"Sexo: {persona_uno.get_sexo()}")
print(f"Peso: {persona_uno.get_peso()}")
print(f"Altura: {persona_uno.get_altura()}")

# Usando los setters
persona_uno.set_nombre("Juan")
persona_uno.set_edad(30)
persona_uno.set_DNI(987654321)
persona_uno.set_sexo("M")
persona_uno.set_peso(70)
persona_uno.set_altura(1.80)

# Usando los métodos
persona_uno.calcularIMC()
persona_uno.esMayorDeEdad()
persona_uno.comprobarSexo("M")
persona_uno.get_DIAN()
persona_uno.set_DIAN("1088357367")
persona_uno.metodo_publico()
