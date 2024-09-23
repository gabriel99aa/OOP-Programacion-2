class Dragon:
    __dragon_type = "Aire"

    def __init__(self):
        self.__acc_energia = 0
        self.__edad = 0
        self.__peso = 1000
        self.__altura = 10
        self.__nivel_fuego = 50

    # Getters y Setters
    def get_acc_energia(self):
        return self.__acc_energia

    def set_acc_energia(self, energia):
        self.__acc_energia = energia

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_nivel_fuego(self):
        return self.__nivel_fuego

    def set_nivel_fuego(self, nivel):
        self.__nivel_fuego = nivel

    def get_dragon_type(self):
        return print(f"Tipo: {self.__dragon_type}")

    def set_dragon_type(self, tipo):
        self.__dragon_type = tipo
        return self.get_dragon_type()

    # Métodos privados
    def __controlar_fuego(self):
        if self.__nivel_fuego > 100:
            self.__nivel_fuego = 100
        elif self.__nivel_fuego < 0:
            self.__nivel_fuego = 0

    def __restaurar_energia(self):
        if self.__acc_energia > 1000:
            self.__acc_energia = 1000

    def __verificar_debilidad(self):
        if self.__acc_energia < 50:
            return True
        return False

    def __verificar_felicidad(self):
        return 500 <= self.__acc_energia <= 1000

    def __calcular_distancia_vuelo(self):
        if 300 <= self.__acc_energia <= 400:
            if self.__acc_energia % 20 == 0:
                return (self.__acc_energia / 5) + 25
            else:
                return (self.__acc_energia / 5) + 10
        return self.__acc_energia / 5

    # Método público que utiliza los 5 métodos privados
    def metodo_publico(self):
        self.__controlar_fuego()
        self.__restaurar_energia()
        debil = self.__verificar_debilidad()
        feliz = self.__verificar_felicidad()
        distancia = self.__calcular_distancia_vuelo()

        print(f"Energía actual: {self.__acc_energia}")
        if debil:
            print("El dragón está débil.")
        if feliz:
            print("El dragón está feliz.")
        print(f"El dragón quiere volar {distancia} kilómetros.")

    def comer(self, gramos):
        self.__acc_energia += gramos * 4
        self.__restaurar_energia()

    def volar(self, kilometros):
        self.__acc_energia -= kilometros + 10
        self.__restaurar_energia()

    def energia(self):
        print(f"La energía del dragón es: {self.__acc_energia}")

    def estaDebil(self):
        if self.__verificar_debilidad():
            print(f"El dragón está débil - Energía: {self.__acc_energia}")

    def estaFeliz(self):
        if self.__verificar_felicidad():
            print(f"El dragón está feliz - Energía: {self.__acc_energia}")

    def cuantoQuiereVolar(self):
        distancia = self.__calcular_distancia_vuelo()
        print(f"El dragón quiere volar {distancia} kilómetros")


print("Tener en cuenta que la comida se ingresa en gramos")
print("Tener en cuenta que la distancia de vuelo se mide en kilómetros")
print()

# P.ej. si se evalúa la siguiente secuencia
Chimuela = Dragon()
Chimuela.comer(85)
Chimuela.energia()  # Resultado debe ser 340
Chimuela.estaDebil()
Chimuela.estaFeliz()
Chimuela.cuantoQuiereVolar()

print()
Chimuela_2 = Dragon()
Chimuela_2.estaDebil()
Chimuela_2.estaFeliz()
Chimuela_2.cuantoQuiereVolar()

print()
Chimuela_3 = Dragon()
Chimuela_3.comer(200)
Chimuela_3.estaDebil()
Chimuela_3.estaFeliz()
Chimuela_3.cuantoQuiereVolar()

Chimuela_3.get_dragon_type()
Chimuela_3.set_dragon_type("Marino")
Chimuela_3.metodo_publico()
