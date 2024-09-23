class Contador:
    __range = "-100 a 1000"

    def __init__(self):
        self.__contador = 0
        self.__ultimo_comando_str = ""
        self.__min = -100
        self.__max = 1000
        self.__step = 1

    # Getters y setters
    def get_contador(self):
        return self.__contador

    def set_contador(self, valor):
        self.__contador = valor

    def get_ultimo_comando(self):
        return self.__ultimo_comando_str

    def set_ultimo_comando(self, comando):
        self.__ultimo_comando_str = comando

    def get_min(self):
        return self.__min

    def set_min(self, valor):
        self.__min = valor

    def get_max(self):
        return self.__max

    def set_max(self, valor):
        self.__max = valor

    def get_step(self):
        return self.__step

    def set_step(self, valor):
        self.__step = valor

    def get_range(self):
        return print(f"Rango: {self.__range}")

    def set_range(self, since, until):
        self.__range = f"{since} a {until}"
        return self.get_range()

    # Métodos privados
    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def __verificar_rango(self):
        return self.__min <= self.__contador <= self.__max

    def __incrementar(self):
        self.__contador += self.__step
        self.__ultimo_comando_str = "incremento"

    def __decrementar(self):
        self.__contador -= self.__step
        self.__ultimo_comando_str = "decremento"

    def __resetear(self):
        self.__contador = 0
        self.__ultimo_comando_str = "reset"

    # Método público que utiliza los 5 métodos privados
    def metodo_publico(self):
        print(self.__metodo_privado())
        self.__incrementar()
        self.__decrementar()
        self.__resetear()
        print(f"El valor está en rango: {'Sí' if self.__verificar_rango() else 'No'}")

    def reset(self):
        self.__resetear()

    def inc(self):
        self.__incrementar()

    def dec(self):
        self.__decrementar()

    def valor_actual(self, nuevo_valor=None):
        if nuevo_valor is None:
            print(f"El valor actual es: {self.__contador}")
        else:
            self.__contador = nuevo_valor
            self.__ultimo_comando_str = "actualizacion"

    def ultimo_comando(self):
        print(f"El último comando fue: {self.__ultimo_comando_str}")


# P.ej. si se evalúa la siguiente secuencia
contador_uno = Contador()
contador_uno.valor_actual(10)
contador_uno.inc()
contador_uno.inc()
contador_uno.dec()
contador_uno.inc()
contador_uno.ultimo_comando()
contador_uno.valor_actual()
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
contador_cuatro.get_range()
contador_cuatro.set_range(-200, 300)
contador_cuatro.metodo_publico()
