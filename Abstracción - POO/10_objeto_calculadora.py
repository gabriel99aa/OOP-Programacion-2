class Calculadora:
    __marca = "CASIO"

    def __init__(self):
        self.valor = 0

    def get_marca(self):
        return print(f"MARCA: {self.__marca}")

    def set_marca(self, marca):
        self.__marca = marca
        return self.get_marca()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

    def cargar(self, numero):
        self.valor = numero

    def sumar(self, numero):
        self.valor += numero

    def restar(self, numero):
        self.valor -= numero

    def multiplicar(self, numero):
        self.valor *= numero

    def valorActual(self):
        print(f"El valor actual es: {self.valor}")


calculadora = Calculadora()
# P.ej. si se evalúa la siguiente secuencia
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()
# el resultado debe ser 24.
calculadora.get_marca()
calculadora.set_marca("CHINA")
calculadora.metodo_publico()
