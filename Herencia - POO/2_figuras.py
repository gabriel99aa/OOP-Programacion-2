class Figuras:
    def __init__(self, peso, color, nombre):
        self.peso = (peso,)
        self.color = color
        self.nombre = nombre


class Cuadrado(Figuras):
    def __init__(self, lado_izquierdo, lado_abajo, peso, color, nombre):
        super().__init__(peso, color, nombre)
        self.lado_izquierdo = lado_izquierdo
        self.lado_abajo = lado_abajo

    def calcular_area(self):
        return print(f"El area es: {self.lado_izquierdo * self.lado_abajo}")


class Circulo(Figuras):
    def __init__(self, peso, color, nombre, radio):
        super().__init__(peso, color, nombre)
        self.radio = radio

    def calcular_area(self):
        PI = 3.14159
        return print(f"El area es: {PI * pow(self.radio, 2)}")


class Triangulo(Figuras):
    def __init__(self, peso, color, nombre, base, altura):
        super().__init__(peso, color, nombre)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return print(f"El area es: {(self.base * self.altura)/2}")


mi_figura = Figuras(2, "red", "laptop")

rectangulo = Cuadrado(2, 3, 2, "red", "laptop")
rectangulo.calcular_area()

circulito = Circulo(2, "red", "laptop", 3)
circulito.calcular_area()

triangulito = Triangulo(2, "red", "laptop", 4, 5)
triangulito.calcular_area()
