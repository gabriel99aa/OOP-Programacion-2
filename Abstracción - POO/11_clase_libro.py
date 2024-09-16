class Libro:
    def __init__(self, título, autor, ejemplares=0, prestados=0):
        self.título = título
        self.autor = autor
        self.ejemplares = ejemplares
        self.prestados = prestados

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
