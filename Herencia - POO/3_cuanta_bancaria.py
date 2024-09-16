class Persona:
    def __init__(self, full_name, CC):
        self.full_name = full_name
        self.cc = CC


class Cuenta(Persona):
    def __init__(self, numero_cuenta, saldo, full_name):
        super().__init__(full_name)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def ingresar(self, monto):
        self.saldo += monto
        return print(f"Tú nuevo saldo es: {self.saldo}")

    def retirar(self, monto):
        if self.saldo > monto:
            self.saldo -= monto
            return print(f"Tú nuevo saldo es: {self.saldo}")
        else:
            return print("Fondos insuficientes")

    def actualizar_saldo(self):
        pass


class Cuenta_Corriente(Cuenta):
    def __init__(self, saldo):
        super().__init__(saldo)

    def actualizar_saldo(self):
        self.saldo += self.saldo * 0.015
        return print(f"Actualización de saldo: {self.saldo}")

class Cuenta_Ahorro(Cuenta):
    def __init__(self, saldo, interes):
        super().__init__(saldo)
        self.interes = interes

    def actualizar_saldo(self):
        if(self.saldo >= 1):
            self.saldo += self.saldo * self.interes
            return print(f"Actualización de saldo: {self.saldo}")
        else:
            return print("No tiene saldo minimo de 1")