class Nave_espacial:
    def __init__(self):
        self.__potencia = 50
        self.__coraza = 5
        self.__galaxia = "Desconocida"
        self.__estado = "Operativa"
        self.__mision = "Exploración"

    def get_galaxia(self):
        return print(f"GALAXIA: {self.__galaxia}")

    def set_galaxia(self, galaxia):
        self.__galaxia = galaxia
        return self.get_galaxia()

    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, potencia):
        self.__potencia = potencia

    def get_coraza(self):
        return self.__coraza

    def set_coraza(self, coraza):
        self.__coraza = coraza

    def get_estado(self):
        return print(f"ESTADO: {self.__estado}")

    def set_estado(self, estado):
        self.__estado = estado
        return self.get_estado()

    def get_mision(self):
        return print(f"MISIÓN: {self.__mision}")

    def set_mision(self, mision):
        self.__mision = mision
        return self.get_mision()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def __calcular_diferencia_potencia(self):
        return 100 - self.__potencia

    def __calcular_diferencia_coraza(self):
        return 20 - self.__coraza

    def __verificar_estado(self):
        return self.__estado

    def __actualizar_estado(self):
        if self.__potencia <= 0:
            self.__estado = "Desactivada"
        else:
            self.__estado = "Operativa"

    def metodo_publico(self):
        print(f"{self.__metodo_privado()}")
        self.__actualizar_estado()
        print(f"Estado después de método público: {self.__verificar_estado()}")

    def show_potencia(self):
        print(f"La potencia es {self.__potencia}")

    def show_coraza(self):
        print(f"La coraza es {self.__coraza}")

    def encontrarPilaAtomica(self):
        if self.__potencia < 100:
            diferencia = self.__calcular_diferencia_potencia()
            if diferencia >= 25:
                self.__potencia += 25
            else:
                self.__potencia += diferencia

    def encontrarEscudo(self):
        if self.__coraza < 20:
            diferencia = self.__calcular_diferencia_coraza()
            if diferencia >= 10:
                self.__coraza += 10
            else:
                self.__coraza += diferencia

    def recibirAtaque(self, puntos):
        if self.__coraza > 0:
            self.__coraza -= puntos
            if self.__coraza <= 0:
                self.__potencia -= abs(self.__coraza)
                self.__coraza = 0
                if self.__potencia <= 0:
                    self.__potencia = 0
        else:
            self.__potencia -= puntos
            if self.__potencia <= 0:
                self.__potencia = 0


# Ejemplo de uso
enterprise = Nave_espacial()
enterprise.encontrarPilaAtomica()  # Potencia 75
enterprise.recibirAtaque(14)  # Coraza 0, Potencia 66
enterprise.encontrarEscudo()  # Coraza 10
enterprise.show_potencia()  # Potencia 66
enterprise.show_coraza()  # Coraza 10

enterprise.get_galaxia()
enterprise.set_galaxia("Andrómeda")
enterprise.set_estado("En Misión")
enterprise.get_estado()
enterprise.get_mision()
enterprise.set_mision("Defensa")
enterprise.metodo_publico()
