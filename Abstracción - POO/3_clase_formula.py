class Formula:
    __formula_favorita = "NINGUNA"
    __ultima_suma = 0
    __ultimo_fibonacci = []
    __ultimo_primo = 0
    __ultimo_modulo = []

    # Getters y Setters de los atributos privados
    def get_formula_favorita(self):
        return print(f"Fórmula favorita: {self.__formula_favorita}")

    def set_formula_favorita(self, formula_favorita):
        self.__formula_favorita = formula_favorita
        return self.get_formula_favorita()

    def get_ultima_suma(self):
        return print(f"Última suma realizada: {self.__ultima_suma}")

    def set_ultima_suma(self, valor):
        self.__ultima_suma = valor
        return self.get_ultima_suma()

    def get_ultimo_fibonacci(self):
        return print(f"Última secuencia de Fibonacci: {self.__ultimo_fibonacci}")

    def set_ultimo_fibonacci(self, secuencia):
        self.__ultimo_fibonacci = secuencia
        return self.get_ultimo_fibonacci()

    def get_ultimo_primo(self):
        return print(f"Último número primo calculado: {self.__ultimo_primo}")

    def set_ultimo_primo(self, primo):
        self.__ultimo_primo = primo
        return self.get_ultimo_primo()

    def get_ultimo_modulo(self):
        return print(f"Últimos números módulo 2: {self.__ultimo_modulo}")

    def set_ultimo_modulo(self, modulos):
        self.__ultimo_modulo = modulos
        return self.get_ultimo_modulo()

    # Métodos privados
    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def __calcular_suma(self, a, b):
        return a + b

    def __calcular_fibonacci(self, cantidad):
        if cantidad <= 0:
            return []
        elif cantidad == 1:
            return [0]
        elif cantidad == 2:
            return [0, 1]

        fib_sequence = [0, 1]
        while len(fib_sequence) < cantidad:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def __es_primo(self, n):
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

    def __calcular_primos(self, limite):
        primos = []
        for num in range(2, limite + 1):
            if self.__es_primo(num):
                primos.append(num)
        return primos

    def __calcular_multiplos(self, limite):
        return [i for i in range(1, limite + 1) if i % 2 == 0]

    def metodo_publico(self):
        suma = self.__calcular_suma(3, 5)
        fibonacci = self.__calcular_fibonacci(5)
        primos = self.__calcular_primos(10)
        multiplos = self.__calcular_multiplos(10)

        self.set_ultima_suma(suma)
        self.set_ultimo_fibonacci(fibonacci)
        self.set_ultimo_primo(primos[-1])
        self.set_ultimo_modulo(multiplos)

        print(f"Suma: {suma}")
        print(f"Fibonacci: {fibonacci}")
        print(f"Primos: {primos}")
        print(f"Múltiplos de 2: {multiplos}")

    def sumar(self, entero_uno, entero_dos):
        resultado = self.__calcular_suma(entero_uno, entero_dos)
        self.set_ultima_suma(resultado)
        print(f"El resultado de la suma es: {resultado}")

    def fibonacci(self, cantidad):
        secuencia = self.__calcular_fibonacci(cantidad)
        self.set_ultimo_fibonacci(secuencia)
        print(f"fibonacci: {secuencia}")

    def operacion_modulo(self, cantidad):
        modulos = self.__calcular_multiplos(cantidad)
        self.set_ultimo_modulo(modulos)
        print(f"Números del 1 a {cantidad} que tienen residuo 0:")
        for numero in modulos:
            print(numero)

    def primos(self, cantidad):
        primos = self.__calcular_primos(cantidad)
        if primos:
            self.set_ultimo_primo(primos[-1])
        print(f"Números primos hasta {cantidad}: {primos}")


formula = Formula()

# Usar los métodos públicos
formula.sumar(20, 30)
formula.fibonacci(10)
formula.operacion_modulo(20)
formula.primos(10)
formula.metodo_publico()

# Usar los getters para ver los valores de los atributos privados
formula.get_formula_favorita()
formula.get_ultima_suma()
formula.get_ultimo_fibonacci()
formula.get_ultimo_primo()
formula.get_ultimo_modulo()

# Usar los setters para modificar los atributos privados
formula.set_formula_favorita("Fibonacci")
formula.set_ultima_suma(100)
formula.set_ultimo_fibonacci([0, 1, 1, 2, 3, 5])
formula.set_ultimo_primo(7)
formula.set_ultimo_modulo([2, 4, 6, 8, 10])
