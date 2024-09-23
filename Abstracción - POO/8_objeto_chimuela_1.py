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
    def __metabolismo(self):
        return self.__peso * 0.1

    def __controlar_fuego(self):
        if self.__nivel_fuego > 100:
            self.__nivel_fuego = 100
        elif self.__nivel_fuego < 0:
            self.__nivel_fuego = 0

    def __volar_distancia(self, distancia):
        self.__acc_energia -= distancia + 10

    def __consumir_comida(self, gramos):
        self.__acc_energia += gramos * 4

    def __verificar_energia(self):
        if self.__acc_energia < 0:
            self.__acc_energia = 0

    # Método público que utiliza los 5 métodos privados
    def metodo_publico(self):
        print("Controlando energía del dragón...")
        self.__controlar_fuego()
        self.__volar_distancia(50)
        self.__consumir_comida(100)
        self.__verificar_energia()
        print(f"Energía tras ajustes: {self.__acc_energia}")
        print(f"Nivel de fuego ajustado: {self.__nivel_fuego}")
        print(self.__metabolismo())

    def comer(self, gramos):
        self.__consumir_comida(gramos)

    def volar(self, kilometros):
        self.__volar_distancia(kilometros)

    def energia(self):
        print(f"La energía del dragón es: {self.__acc_energia}")


print("Tener en cuenta que la comida se ingresa en gramos")
print("Tener en cuenta que la distancia de vuelo se mide en kilómetros")
print()

Chimuela = Dragon()
Chimuela.comer(100)
Chimuela.volar(10)
Chimuela.volar(20)
Chimuela.energia()

Chimuela.get_dragon_type()
Chimuela.set_dragon_type("Tierra")
Chimuela.metodo_publico()
