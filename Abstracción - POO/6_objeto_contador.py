class Contador:
    __range = "-100 a 1000"

    def __init__(self):
        self.contador = 0

    def get_range(self):
        return print(f"Rango: {self.__range}")

    def set_range(self, since, until):
        self.__range = f"{since} a {until}"
        return self.get_range()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

    def reset(self):
        self.contador = 0

    def inc(self):
        self.contador += 1

    def dec(self):
        self.contador -= 1

    def valor_actual(self, nuevo_valor=None):
        if nuevo_valor is None:
            print(f"El valor actual es: {self.contador}")
        else:
            self.contador = nuevo_valor


# P.ej. si se evalúa la siguiente secuencia
contador_uno = Contador()
contador_uno.valor_actual(10)
contador_uno.inc()
contador_uno.inc()
contador_uno.dec()
contador_uno.inc()
contador_uno.valor_actual()
# el resultado debe ser 12.
print()
# P.ej. si se evalúa la siguiente secuencia
contador_dos = Contador()
contador_dos.valor_actual(17)
contador_dos.dec()
contador_dos.dec()
contador_dos.dec()
contador_dos.inc()
contador_dos.valor_actual()
# el resultado debe ser 15.
print()
# P.ej. si se evalúa la siguiente secuencia
contador_tres = Contador()
contador_tres.valor_actual(1)
contador_tres.inc()
contador_tres.dec()
contador_tres.dec()
contador_tres.inc()
contador_tres.valor_actual()
# el resultado debe ser 1.
contador_tres.get_range()
contador_tres.set_range(-200, 300)
contador_tres.metodo_publico()
