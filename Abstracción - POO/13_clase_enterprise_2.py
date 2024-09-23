class Nave_espacial:
    def __init__(self):
        self.__potencia = 50  # Atributo privado
        self.__coraza = 5  # Atributo privado
        self.__galaxia = "Desconocida"  # Atributo privado
        self.__tipo_mision = "Exploración"  # Atributo privado
        self.__nombre_nave = "Enterprise"  # Atributo privado

    def get_galaxia(self):
        return print(f"GALAXIA: {self.__galaxia}")

    def set_galaxia(self, galaxia):
        self.__galaxia = galaxia
        return self.get_galaxia()

    def get_tipo_mision(self):
        return self.__tipo_mision

    def set_tipo_mision(self, tipo_mision):
        self.__tipo_mision = tipo_mision

    def get_nombre_nave(self):
        return self.__nombre_nave

    def set_nombre_nave(self, nombre_nave):
        self.__nombre_nave = nombre_nave

    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, potencia):
        self.__potencia = potencia

    def get_coraza(self):
        return self.__coraza

    def set_coraza(self, coraza):
        self.__coraza = coraza

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def __calcular_fortaleza_defensiva(self):
        return self.__coraza + self.__potencia

    def __verificar_necesidad_fortalecerse(self):
        return self.__coraza == 0 and self.__potencia < 20

    def __calcular_fortaleza_ofensiva(self):
        if self.__potencia < 20:
            return 0
        else:
            return (self.__potencia - 20) / 2

    def __actualizar_estado(self):
        estado = "Operativa" if self.__potencia > 0 else "Inoperativa"
        print(f"Estado de la nave: {estado}")

    def metodo_publico(self):
        print(f"{self.__metodo_privado()}")
        fortaleza_defensiva = self.__calcular_fortaleza_defensiva()
        necesita_fortalecerse = self.__verificar_necesidad_fortalecerse()
        fortaleza_ofensiva = self.__calcular_fortaleza_ofensiva()

        print(f"Fortaleza defensiva: {fortaleza_defensiva}")
        print(f"Necesita fortalecerse: {necesita_fortalecerse}")
        print(f"Fortaleza ofensiva: {fortaleza_ofensiva}")
        print(f"Tipo de misión: {self.__tipo_mision}")
        print(f"Nombre de la nave: {self.__nombre_nave}")
        self.__actualizar_estado()

    def show_potencia(self):
        print(f"La potencia es {self.__potencia}")

    def show_coraza(self):
        print(f"La coraza es {self.__coraza}")

    def encontrarPilaAtomica(self):
        if self.__potencia < 100:
            diferencia = 100 - self.__potencia
            if diferencia >= 25:
                self.__potencia += 25
            else:
                self.__potencia += diferencia

    def encontrarEscudo(self):
        if self.__coraza < 20:
            diferencia = 20 - self.__coraza
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

enterprise.show_potencia()
enterprise.show_coraza()

enterprise.get_galaxia()
enterprise.set_galaxia("VIA LÁCTEA")
enterprise.set_tipo_mision("Exploración Avanzada")
enterprise.set_nombre_nave("USS Enterprise")
enterprise.metodo_publico()
