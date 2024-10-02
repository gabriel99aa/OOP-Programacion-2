class PilaStack:
    def __init__(self):
        self.elementos = []

    def enpilar(self, elemento):
        self.elementos.append(elemento)

    def desenpilar(self):
        if self.elementos:
            return self.elementos.pop()
        return None

    def longitud(self):
        return len(self.elementos)

    def ver_proximo(self):
        if self.elementos:
            return self.elementos[-1]
        return None

    def ver_elementos(self):
        return self.elementos

    def ejercicio1(self, numero):
        for i in range(1, numero + 1):
            self.enpilar(i)
        # return list(reversed(self.elementos))
        return self.elementos

    def ejercicio2(self):
        if len(self.elementos) == 0:
            return False

        pila_temporal = self.elementos.copy()

        debe_ser_par = True

        while pila_temporal:
            elemento = pila_temporal.pop()

            if not isinstance(elemento, int):
                return False

            if debe_ser_par:
                if elemento % 2 != 0:
                    return False
            else:
                if elemento % 2 != 1:
                    return False

            debe_ser_par = not debe_ser_par

        return True

    def ejercicio3(self):
        suma_total = 0

        pila_temporal = self.elementos.copy()

        while pila_temporal:
            elemento = pila_temporal.pop()
            if isinstance(elemento, (int, float)):
                suma_total += elemento

        return suma_total

    def ejercicio4(self):
        arreglo = []

        pila_temporal = self.elementos.copy()

        while pila_temporal:
            elemento = pila_temporal.pop()
            if isinstance(elemento, int) and elemento % 2 == 0:
                arreglo.append(elemento)

        return arreglo

    def ejercicio5(self):
        arreglo = []

        pila_temporal = self.elementos.copy()

        while pila_temporal:
            elemento = pila_temporal.pop()
            if isinstance(elemento, int) and elemento % 2 != 0:
                arreglo.append(elemento)

        return arreglo

    def ejercicio6(self):
        arreglo = []

        pila_temporal = self.elementos.copy()

        while pila_temporal:
            elemento = pila_temporal.pop()
            if isinstance(elemento, str):
                arreglo.append(elemento)

        return arreglo

    def ejercicio7(self):
        cantidades = {"strings": 0, "numbers": 0, "arrays": 0}

        pila_temporal = self.elementos.copy()

        while pila_temporal:
            elemento = pila_temporal.pop()
            if isinstance(elemento, str):
                cantidades["strings"] += 1
            if isinstance(elemento, (int, float)):
                cantidades["numbers"] += 1
            if isinstance(elemento, list):
                cantidades["arrays"] += 1

        return cantidades

    def ejercicio8(self, nombre_elemento):
        pila_temporal = []
        elemento_eliminado = False

        while self.elementos:
            elemento = self.desenpilar()

            if elemento != nombre_elemento:
                pila_temporal.append(elemento)
            else:
                elemento_eliminado = True

        if not elemento_eliminado:
            print(f"Elemento '{nombre_elemento}' no se encontró en la pila.")
        else:
            print(f"Elemento '{nombre_elemento}' eliminado de la pila.")

        return pila_temporal

    def ejercicio9(self, posicion):
        if posicion < 0 or posicion >= len(self.elementos):
            print(f"Posición '{posicion}' no existe en la pila.")
            return self.elementos

        self.elementos.pop(-posicion)

        return list(reversed(self.elementos))

    def ejercicio10(self, posicion):
        arreglo = []

        for index in range(len(self.elementos)):
            elemento = self.desenpilar()

            if index >= posicion:
                arreglo.append(elemento)

        return arreglo
