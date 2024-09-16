class Cuenta:
    def __init__(self, titular, cantidad=0, password=""):
        self.titular = titular
        self.cantidad = cantidad
        self.__password = password

    def get_password(self):
        return print(f"Password: {self.__password}")

    def set_password(self, password):
        self.__password = password
        return self.get_password()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

    def mostrar(self):
        print(
            f"El titular de la cuenta es: {self.titular} \n y su cantidad es: {self.cantidad}"
        )

    def ingresar(self, cantidad_ingresar):
        if cantidad_ingresar < 1:
            print("La cantidad ingresada no es un valor válido")
        else:
            nueva_cantidad = self.cantidad + cantidad_ingresar
            print(
                f"La cantidad ingresada fue: {cantidad_ingresar} \n su saldo anterior era: {self.cantidad} \n y su nueva cantidad es: {nueva_cantidad}"
            )
            self.cantidad += cantidad_ingresar

    def retirar(self, cantidad_retirar):
        nueva_cantidad = self.cantidad - cantidad_retirar
        print(
            f"La cantidad a retirar es: {cantidad_retirar} \n su saldo anterior era: {self.cantidad} \n y su nueva cantidad es: {nueva_cantidad}"
        )
        self.cantidad -= cantidad_retirar


cuenta_uno = Cuenta("Sebastian")

cuenta_uno.mostrar()
print("\n")
cuenta_uno.ingresar(100000)
print("\n")
cuenta_uno.retirar(49000)

print("-------------------------- \n")

cuenta_dos = Cuenta("Gabriel", 200000)

cuenta_dos.mostrar()
print("\n")
cuenta_dos.ingresar(50000)
print("\n")
cuenta_dos.retirar(40000)

cuenta_dos.set_password("314235HU86")
cuenta_dos.metodo_publico()
cuenta_dos.get_password()
