class Formula:
    def sumar(self, entero_uno, entero_dos):
        print(f"El resultado de la suma es: {entero_uno + entero_dos}")

    def fibonacci(self, cantidad):
        if cantidad <= 0:
            return []
        elif cantidad == 1:
            return [0]
        elif cantidad == 2:
            return [0, 1]

        fib_sequence = [0, 1]

        while len(fib_sequence) < cantidad:
            next_value = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_value)

        return print(f"fibonacci: {fib_sequence}")

    def operacion_modulo(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return

        print(f"Números del 1 a {cantidad} que tienen residuo 0:")
        for i in range(1, cantidad + 1):
            if i % 2 == 0:
                print(i)

    def es_primo(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def primos(self, cantidad):
        if cantidad < 2:
            print("No hay números primos menores que 2.")
            return

        print(f"Números primos hasta {cantidad}:")
        for num in range(2, cantidad + 1):
            if self.es_primo(num):
                print(num, end=" ")
        print()


suma = Formula()
suma.sumar(20, 30)

fibonacci = Formula()
fibonacci.fibonacci(10)

operacion_modulo = Formula()
operacion_modulo.operacion_modulo(100)

primos = Formula()
primos.primos(10)
