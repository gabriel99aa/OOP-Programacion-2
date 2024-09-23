class Libro:
    def __init__(self, título, autor, ejemplares=0, prestados=0, donado=False):
        self.__título = título
        self.__autor = autor
        self.__ejemplares = ejemplares
        self.__prestados = prestados
        self.__donado = donado

    # Getters y setters
    def get_título(self):
        return self.__título

    def set_título(self, título):
        self.__título = título

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_donado(self):
        return print(f"DONADO: {self.__donado}")

    def set_donado(self, donado):
        self.__donado = donado
        return self.get_donado()

    def get_ejemplares(self):
        return self.__ejemplares

    def set_ejemplares(self, ejemplares):
        self.__ejemplares = ejemplares

    def get_prestados(self):
        return self.__prestados

    def set_prestados(self, prestados):
        self.__prestados = prestados

    # Métodos privados
    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def __calcular_disponibles(self):
        return self.__ejemplares - self.__prestados

    def __puede_prestar(self):
        return self.__calcular_disponibles() > 0

    def __puede_devolver(self):
        return self.__prestados > 0

    def __estado_libro(self):
        estado = "Donado" if self.__donado else "No Donado"
        return f"Estado del libro: {estado}"

    def metodo_publico(self):
        print(
            f"{self.__metodo_privado()} | Título: {self.__título}, Autor: {self.__autor}, {self.__estado_libro()}"
        )

    def préstamo(self):
        if self.__puede_prestar():
            print(True)
            disponibles = self.__calcular_disponibles()
            print(f"Ejemplares disponibles: {disponibles - 1}")
            self.__prestados += 1
        else:
            print(False)
            print("Ya no hay ejemplares disponibles")

    def devolucion(self):
        if self.__puede_devolver():
            print(True)
            disponibles = self.__calcular_disponibles()
            print(f"Ejemplares disponibles: {disponibles + 1}")
            self.__prestados -= 1
        else:
            print(False)
            print("No se puede devolver libros que no se hayan prestado.")
            disponibles = self.__calcular_disponibles()
            print(f"Ejemplares disponibles: {disponibles}")


# Ejemplo de uso
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
