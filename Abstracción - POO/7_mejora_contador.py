class Contador:
    __range = "-100 a 1000"

    def __init__(self):
        self.contador = 0
        self.ultimo_comando_str = ""

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
        self.ultimo_comando_str = "reset"

    def inc(self):
        self.contador += 1
        self.ultimo_comando_str = "incremento"

    def dec(self):
        self.contador -= 1
        self.ultimo_comando_str = "decremento"

    def valor_actual(self, nuevo_valor=None):
        if nuevo_valor is None:
            print(f"El valor actual es: {self.contador}")
        else:
            self.contador = nuevo_valor
            self.ultimo_comando_str = "actualizacion"

    def ultimo_comando(self):
        print(f"El ultimo comando fue: {self.ultimo_comando_str}")


# P.ej. si se evalúa la siguiente secuencia
contador_uno = Contador()
contador_uno.valor_actual(10)
contador_uno.inc()
contador_uno.inc()
contador_uno.dec()
contador_uno.inc()
contador_uno.ultimo_comando()
contador_uno.valor_actual()
# el resultado debe ser 12.
print()
# P.ej. si se evalúa la siguiente secuencia
contador_dos = Contador()
contador_dos.valor_actual(17)
contador_dos.dec()
contador_dos.ultimo_comando()
contador_dos.dec()
contador_dos.dec()
contador_dos.inc()
contador_dos.valor_actual()
# el resultado debe ser 15.
print()
# P.ej. si se evalúa la siguiente secuencia
contador_tres = Contador()
contador_tres.valor_actual(1)
contador_tres.ultimo_comando()
contador_tres.inc()
contador_tres.dec()
contador_tres.dec()
contador_tres.inc()
contador_tres.valor_actual()
# el resultado debe ser 1.
print()
# P.ej. si se evalúa la siguiente secuencia
contador_cuatro = Contador()
contador_cuatro.valor_actual(100)
contador_cuatro.inc()
contador_cuatro.valor_actual()
contador_cuatro.dec()
contador_cuatro.reset()
contador_cuatro.ultimo_comando()
contador_cuatro.valor_actual()
# el resultado debe ser 0.
contador_cuatro.get_range()
contador_cuatro.set_range(-200, 300)
contador_cuatro.metodo_publico()
