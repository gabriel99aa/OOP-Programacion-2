class Dragon:
    def __init__(self):
        self.acc_energia = 0

    def comer(self, gramos):
        self.acc_energia = gramos * 4

    def volar(self, kilometros):
        self.acc_energia = self.acc_energia - kilometros - 10

    def energia(self):
        print(f"La energía del dragon es: {self.acc_energia}")

    def estaDebil(self):
        if self.acc_energia < 50:
            print(f"El dragon está débil - Energia: {self.acc_energia}")

    def estaFeliz(self):
        if self.acc_energia >= 500 and self.acc_energia <= 1000:
            print(f"El dragon está felíz - Energia: {self.acc_energia}")

    def cuantoQuiereVolar(self):
        if self.acc_energia >= 300 and self.acc_energia <= 400:
            if self.acc_energia % 20 == 0:
                wise = (self.acc_energia / 5) + 25
                print(f"El dragon quiere volar {wise} kilómetros")
            else:
                wise = (self.acc_energia / 5) + 10
                print(f"El dragon quiere volar {wise} kilómetros")
        else:
            print(f"El dragon quiere volar {self.acc_energia / 5} kilómetros")


print("Tener en cuanta que la comida se ingresa en gramos")
print(
    "Tener en cuanta que la la distancia de vuelo se mide y se debe ingresar en kilometros"
)
print()
Chimuela = Dragon()
# P.ej. se evalúa la siguiente secuencia
Chimuela.comer(85)
Chimuela.energia()
# el resultado debe ser 340.
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
