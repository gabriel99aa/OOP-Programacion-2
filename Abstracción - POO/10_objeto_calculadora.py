class Calculadora:
    def __init__(self):
        self.valor = 0

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
