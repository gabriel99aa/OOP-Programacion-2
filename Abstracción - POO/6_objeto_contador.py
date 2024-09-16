class Conatador:
    def __init__(self):
        self.contador = 0

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
contador_uno = Conatador()
contador_uno.valor_actual(10)
contador_uno.inc()
contador_uno.inc()
contador_uno.dec()
contador_uno.inc()
contador_uno.valor_actual()
# el resultado debe ser 12.
print()
# P.ej. si se evalúa la siguiente secuencia
contador_dos = Conatador()
contador_dos.valor_actual(17)
contador_dos.dec()
contador_dos.dec()
contador_dos.dec()
contador_dos.inc()
contador_dos.valor_actual()
# el resultado debe ser 15.
print()
# P.ej. si se evalúa la siguiente secuencia
contador_tres = Conatador()
contador_tres.valor_actual(1)
contador_tres.inc()
contador_tres.dec()
contador_tres.dec()
contador_tres.inc()
contador_tres.valor_actual()
# el resultado debe ser 1.
