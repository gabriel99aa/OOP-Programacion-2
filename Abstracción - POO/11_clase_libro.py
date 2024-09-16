class Libro:
    def __init__(self, título, autor, ejemplares=0, prestados=0, donado=False):
        self.título = título
        self.autor = autor
        self.ejemplares = ejemplares
        self.prestados = prestados
        self.__donado = donado

    def get_donado(self):
        return print(f"DONADO: {self.__donado}")

    def set_donado(self, donado):
        self.__donado = donado
        return self.get_donado()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

    def préstamo(self):
        disponibles = self.ejemplares - self.prestados
        if disponibles > 0:
            print(True)
            print(f"Ejemplares disponibles: {disponibles - 1}")
            self.prestados += 1

        else:
            print(False)
            print("Ya no hay ejemplares disponibles")

    def devolucion(self):
        disponibles = self.ejemplares - self.prestados
        if self.prestados > 0:
            print(True)
            print(f"Ejemplares disponibles: {disponibles + 1}")
            self.prestados -= 1
        else:
            print(False)
            print("No se puede devolver libros que no se hayan prestado.")
            print(f"Ejemplares disponibles: {disponibles}")


libro_1 = Libro("Cien Años", "Gabriel", 10, 0)
libro_1.préstamo()
libro_1.préstamo()
libro_1.préstamo()
libro_1.devolucion()

print()

libro_2 = Libro("Ciencias", "Esteban", 5, 5)
libro_2.préstamo()
libro_2.devolucion()
libro_2.devolucion()
libro_2.préstamo()

libro_2.get_donado()
libro_2.set_donado(True)
libro_2.metodo_publico()
