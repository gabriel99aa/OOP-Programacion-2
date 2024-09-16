class Persona:
    def __init__(self, nombre, edad, DNI, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):
        if self.altura > 3:
            print("Por favor ingrese la altura en metros")

        if self.peso > 200:
            print("Por favor ingrese el peso en kilogramos")

        peso_ideal = self.peso / (self.altura**2)
        # print(f"peso_ideal: {peso_ideal}")

        if peso_ideal < 20:
            print("-1")

        if peso_ideal >= 20 and peso_ideal <= 25:
            print("Esta por debajo de su peso ideal 0")

        if peso_ideal > 25:
            print("Tiene sobrepeso 1")

    def esMayorDeEdad(self):
        if self.edad < 18:
            return print(False)
        else:
            return print(True)

    def comprobarSexo(self, sexo):
        sexos = ["H", "M"]

        if sexo in sexos:
            if self.sexo == sexo:
                print("El sexo es correcto")
            else:
                print(
                    f"El sexo es incorrecto, usted había ingresado previamente: {self.sexo}"
                )
        else:
            print(
                f"Su valor ingresado ({sexo}) no es una opción del sistema \n las opciones del sistema son: {sexos}"
            )


persona_uno = Persona(
    nombre="Gabriel",
    edad=24,
    DNI=29650233528,
    sexo="H",
    peso=66,
    altura=1.76,
)

persona_uno.calcularIMC()
persona_uno.esMayorDeEdad()
persona_uno.comprobarSexo("hombre")
persona_uno.comprobarSexo("M")
persona_uno.comprobarSexo("H")
