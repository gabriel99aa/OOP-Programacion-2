class Nave_espacial:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5
        self.__galaxia = "Desconocida"

    def get_galaxia(self):
        return print(f"GALAXIA: {self.__galaxia}")

    def set_galaxia(self, galaxia):
        self.__galaxia = galaxia
        return self.get_galaxia()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

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

    def fortalezaDefensiva(self):
        print(f"Puede resistir: {self.coraza + self.potencia}")

    def necesitaFortalecerse(self):
        if self.coraza == 0 and self.potencia < 20:
            print(True)
        else:
            print("Aún no necesita fortalecerse")

    def fortalezaOfensiva(self):
        if self.potencia < 20:
            print(f"Puntos de fuerza: {0}")
        elif self.potencia > 20:
            fuerza = (self.potencia - 20) / 2
            print(f"Puntos de fuerza: {fuerza}")


enterprise = Nave_espacial()

enterprise.fortalezaDefensiva()
enterprise.necesitaFortalecerse()
enterprise.fortalezaOfensiva()
print()
enterprise.show_potencia()
enterprise.show_coraza()

enterprise.get_galaxia()
enterprise.set_galaxia("VIA LÁCTEA")
enterprise.metodo_publico()
