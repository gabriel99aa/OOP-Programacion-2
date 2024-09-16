# potencia de 0 a 100 ✅
# nivel de coraza de 0 a 20 ✅
# pila atómica potencia aumenta en 25 ✅
# escudo coraza aumenta en 10 ✅
# ataque_recibido_(puntos) La Enterprise para el ataque con la coraza, y si la coraza no alcanza, el resto se descuenta de la potencia. ✅
# NO puede quedar negativa la potencia ✅
# La coraza no puede quedar negativa ✅
# La Enterprise nace con 50 de potencia y 5 de coraza ✅


class Nave_espacial:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5

    def show_potencia(self):
        print(f"La potencia es {self.potencia}")

    def show_coraza(self):
        print(f"La coraza es {self.coraza}")

    def encontrarPilaAtomica(self):
        if self.potencia < 100:
            diferencia = 100 - self.potencia
            if diferencia >= 25:
                self.potencia += 25
            elif diferencia <= 25:
                self.potencia += diferencia
            else:
                self.potencia += 25

    def encontrarEscudo(self):
        if self.coraza < 20:
            diferencia = 20 - self.coraza
            if diferencia >= 20:
                self.coraza += 10
            elif diferencia <= 10:
                self.coraza += diferencia
            else:
                self.coraza += 10

    def recibirAtaque(self, puntos):
        if self.coraza > 0:
            self.coraza -= puntos
            if self.coraza <= 0:
                self.potencia -= abs(self.coraza)
                self.coraza = 0
                if self.potencia <= 0:
                    self.potencia = 0
        else:
            self.potencia -= puntos
            if self.potencia <= 0:
                self.potencia = 0


enterprise = Nave_espacial()
enterprise.encontrarPilaAtomica()
# Potencia 75
enterprise.recibirAtaque(14)
# Coraza 0
# Potencia 66
enterprise.encontrarEscudo()
# Coraza 10
enterprise.show_potencia()
# Potencia 66
enterprise.show_coraza()
# Coraza 10
