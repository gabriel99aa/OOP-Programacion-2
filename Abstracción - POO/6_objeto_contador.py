class Contador:
    __range = "-100 a 1000"

    def __init__(self):
        self.__contador = 0
        self.__min = -100
        self.__max = 1000
        self.__increment_count = 0
        self.__decrement_count = 0

    # Getters y Setters
    def get_range(self):
        return print(f"Rango: {self.__range}")

    def set_range(self, since, until):
        self.__range = f"{since} a {until}"
        return self.get_range()

    def get_contador(self):
        return self.__contador

    def set_contador(self, value):
        if self.__min <= value <= self.__max:
            self.__contador = value
        else:
            print(
                f"Valor fuera de rango: {value}. Debe estar entre {self.__min} y {self.__max}."
            )

    def get_min(self):
        return self.__min

    def set_min(self, value):
        self.__min = value

    def get_max(self):
        return self.__max

    def set_max(self, value):
        self.__max = value

    def get_increment_count(self):
        return self.__increment_count

    def set_increment_count(self, value):
        self.__increment_count = value

    def get_decrement_count(self):
        return self.__decrement_count

    def set_decrement_count(self, value):
        self.__decrement_count = value

    # Métodos privados
    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def __incrementar_contador(self):
        self.__contador += 1
        self.__increment_count += 1

    def __decrementar_contador(self):
        self.__contador -= 1
        self.__decrement_count += 1

    def __valores_contador(self):
        return self.__contador, self.__increment_count, self.__decrement_count

    def __validar_rango(self):
        return self.__min <= self.__contador <= self.__max

    # Método público que usa los métodos privados
    def metodo_publico(self):
        print(self.__metodo_privado())
        self.__incrementar_contador()
        self.__decrementar_contador()
        valor, inc_count, dec_count = self.__valores_contador()
        print(
            f"Valor actual: {valor}, Incrementos: {inc_count}, Decrementos: {dec_count}"
        )
        print(f"¿Está en rango? {'Sí' if self.__validar_rango() else 'No'}")

    def reset(self):
        self.__contador = 0
        self.set_increment_count(0)
        self.set_decrement_count(0)

    def inc(self):
        self.__incrementar_contador()

    def dec(self):
        self.__decrementar_contador()

    def valor_actual(self, nuevo_valor=None):
        if nuevo_valor is None:
            print(f"El valor actual es: {self.__contador}")
        else:
            self.set_contador(nuevo_valor)


contador_uno = Contador()
contador_uno.valor_actual(10)
contador_uno.inc()
contador_uno.inc()
contador_uno.dec()
contador_uno.inc()
contador_uno.valor_actual()

contador_dos = Contador()
contador_dos.valor_actual(17)
contador_dos.dec()
contador_dos.dec()
contador_dos.dec()
contador_dos.inc()
contador_dos.valor_actual()

contador_tres = Contador()
contador_tres.valor_actual(1)
contador_tres.inc()
contador_tres.dec()
contador_tres.dec()
contador_tres.inc()
contador_tres.valor_actual()
contador_tres.get_range()
contador_tres.set_range(-200, 300)
contador_tres.metodo_publico()
