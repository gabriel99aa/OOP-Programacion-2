class Calculadora:
    __marca = "CASIO"

    def __init__(self):
        self.__valor = 0
        self.__historial_operaciones = []
        self.__memoria = 0
        self.__precision = 2
        self.__estado_bateria = 100

    # Getters y setters
    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_historial(self):
        return self.__historial_operaciones

    def set_historial(self, historial):
        self.__historial_operaciones = historial

    def get_memoria(self):
        return self.__memoria

    def set_memoria(self, valor):
        self.__memoria = valor

    def get_precision(self):
        return self.__precision

    def set_precision(self, precision):
        self.__precision = precision

    def get_estado_bateria(self):
        return self.__estado_bateria

    def set_estado_bateria(self, estado):
        self.__estado_bateria = estado

    def get_marca(self):
        return print(f"MARCA: {self.__marca}")

    def set_marca(self, marca):
        self.__marca = marca
        return self.get_marca()

    # Métodos privados
    def __actualizar_historial(self, operacion, valor):
        self.__historial_operaciones.append(f"{operacion} {valor}")

    def __usar_bateria(self, consumo):
        self.__estado_bateria -= consumo
        if self.__estado_bateria < 0:
            self.__estado_bateria = 0

    def __formatear_resultado(self, valor):
        return round(valor, self.__precision)

    def __recuperar_memoria(self):
        return self.__memoria

    def __guardar_memoria(self, valor):
        self.__memoria = valor
        print(f"Valor {valor} guardado en la memoria.")

    def metodo_publico(self):
        memoria = self.__recuperar_memoria()
        print(f"Memoria: {memoria}")
        print(f"Estado de la batería: {self.__estado_bateria}%")
        print("Historial de operaciones:")
        for operacion in self.__historial_operaciones:
            print(operacion)

    def cargar(self, numero):
        self.__valor = numero
        self.__actualizar_historial("Cargar", numero)
        self.__guardar_memoria(numero)
        self.__usar_bateria(1)

    def sumar(self, numero):
        self.__valor += numero
        self.__actualizar_historial("Sumar", numero)
        self.__guardar_memoria(self.__valor)
        self.__usar_bateria(1)

    def restar(self, numero):
        self.__valor -= numero
        self.__actualizar_historial("Restar", numero)
        self.__guardar_memoria(self.__valor)
        self.__usar_bateria(1)

    def multiplicar(self, numero):
        self.__valor *= numero
        self.__actualizar_historial("Multiplicar", numero)
        self.__guardar_memoria(self.__valor)
        self.__usar_bateria(2)

    def valorActual(self):
        resultado = self.__formatear_resultado(self.__valor)
        print(f"El valor actual es: {resultado}")
        self.__usar_bateria(1)


calculadora = Calculadora()

# P.ej. si se evalúa la siguiente secuencia
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()  # El resultado debe ser 24.

calculadora.get_marca()
calculadora.set_marca("CHINA")
calculadora.metodo_publico()
