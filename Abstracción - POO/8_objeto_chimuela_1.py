class Dragon:
    __dragon_type = "Aire"

    def __init__(self):
        self.acc_energia = 0

    def get_dragon_type(self):
        return print(f"Tipo: {self.__dragon_type}")

    def set_dragon_type(self, type):
        self.__dragon_type = type
        return self.get_dragon_type()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

    def comer(self, gramos):
        self.acc_energia = gramos * 4

    def volar(self, kilometros):
        self.acc_energia = self.acc_energia - kilometros - 10

    def energia(self):
        print(f"La energía del dragon es: {self.acc_energia}")


print("Tener en cuanta que la comida se ingresa en gramos")
print(
    "Tener en cuanta que la la distancia de vuelo se mide y se debe ingresar en kilometros"
)
print()
Chimuela = Dragon()
# P.ej. se evalúa la siguiente secuencia
Chimuela.comer(100)
Chimuela.volar(10)
Chimuela.volar(20)
Chimuela.energia()
# el resultado debe ser 350.
Chimuela.get_dragon_type()
Chimuela.set_dragon_type("Tierra")
Chimuela.metodo_publico()
