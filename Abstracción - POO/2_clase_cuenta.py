class Cuenta:
    def __init__(self, titular, cantidad=0, password=""):
        self.__titular = titular
        self.__cantidad = cantidad
        self.__password = password
        self.__tipo_cuenta = "Ahorros"
        self.__interes = 0.02

    # Getters y Setters para los 5 atributos privados
    def get_titular(self):
        return print(f"Titular: {self.__titular}")

    def set_titular(self, titular):
        self.__titular = titular
        return self.get_titular()

    def get_cantidad(self):
        return print(f"Cantidad: {self.__cantidad}")

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
        return self.get_cantidad()

    def get_password(self):
        return print(f"Password: {self.__password}")

    def set_password(self, password):
        self.__password = password
        return self.get_password()

    def get_tipo_cuenta(self):
        return print(f"Tipo de cuenta: {self.__tipo_cuenta}")

    def set_tipo_cuenta(self, tipo_cuenta):
        self.__tipo_cuenta = tipo_cuenta
        return self.get_tipo_cuenta()

    def get_interes(self):
        return print(f"Interés: {self.__interes}")

    def set_interes(self, interes):
        self.__interes = interes
        return self.get_interes()

    # Métodos privados
    def __calcular_interes(self):
        return self.__cantidad * self.__interes

    def __verificar_saldo(self, cantidad):
        return self.__cantidad >= cantidad

    def __proteger_contrasena(self, contrasena):
        return self.__password == contrasena

    def __generar_numero_cuenta(self):
        return f"Cuenta-{hash(self.__titular) % 10000}"

    def __actualizar_saldo(self, monto):
        self.__cantidad += monto

    # Método público que utiliza los métodos privados
    def metodo_publico(self, contrasena):
        if self.__proteger_contrasena(contrasena):
            numero_cuenta = self.__generar_numero_cuenta()
            interes_ganado = self.__calcular_interes()
            print(f"Número de cuenta: {numero_cuenta}")
            print(f"Interés ganado: {interes_ganado}")
            return f"Saldo actual con intereses: {self.__cantidad + interes_ganado}"
        else:
            return "Contraseña incorrecta"

    # Método público para mostrar la cuenta
    def mostrar(self):
        print(
            f"El titular de la cuenta es: {self.__titular} \n y su cantidad es: {self.__cantidad}"
        )

    # Método para ingresar dinero
    def ingresar(self, cantidad_ingresar):
        if cantidad_ingresar < 1:
            print("La cantidad ingresada no es válida.")
        else:
            self.__actualizar_saldo(cantidad_ingresar)
            print(
                f"La cantidad ingresada fue: {cantidad_ingresar} \n Nuevo saldo: {self.__cantidad}"
            )

    # Método para retirar dinero
    def retirar(self, cantidad_retirar, contrasena):
        if self.__proteger_contrasena(contrasena):
            if self.__verificar_saldo(cantidad_retirar):
                self.__actualizar_saldo(-cantidad_retirar)
                print(
                    f"La cantidad a retirar es: {cantidad_retirar} \n Saldo restante: {self.__cantidad}"
                )
            else:
                print("Fondos insuficientes.")
        else:
            print("Contraseña incorrecta.")


# Ejemplo de uso de todos los métodos y getters/setters
cuenta_uno = Cuenta("Sebastian", 100000, "314235HU86")

# Usar todos los métodos públicos
cuenta_uno.mostrar()
cuenta_uno.ingresar(50000)
cuenta_uno.retirar(40000, "314235HU86")
cuenta_uno.metodo_publico("314235HU86")

# Usar los getters
cuenta_uno.get_titular()
cuenta_uno.get_cantidad()
cuenta_uno.get_password()
cuenta_uno.get_tipo_cuenta()
cuenta_uno.get_interes()

# Usar los setters
cuenta_uno.set_titular("Juan")
cuenta_uno.set_cantidad(200000)
cuenta_uno.set_password("newpassword123")
cuenta_uno.set_tipo_cuenta("Corriente")
cuenta_uno.set_interes(0.03)

print("\n--------------------------\n")

# Segunda cuenta
cuenta_dos = Cuenta("Gabriel", 200000, "contraseña123")

# Usar todos los métodos públicos
cuenta_dos.mostrar()
cuenta_dos.ingresar(100000)
cuenta_dos.retirar(50000, "contraseña123")
cuenta_dos.metodo_publico("contraseña123")

# Usar los getters
cuenta_dos.get_titular()
cuenta_dos.get_cantidad()
cuenta_dos.get_password()
cuenta_dos.get_tipo_cuenta()
cuenta_dos.get_interes()

# Usar los setters
cuenta_dos.set_titular("Maria")
cuenta_dos.set_cantidad(350000)
cuenta_dos.set_password("nuevacontraseña")
cuenta_dos.set_tipo_cuenta("Corriente")
cuenta_dos.set_interes(0.05)
