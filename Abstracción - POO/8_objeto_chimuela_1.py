class Dragon:
    def __init__(self):
        self.acc_energia = 0

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
