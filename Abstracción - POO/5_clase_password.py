import random
import string


class Password:
    __recomendation = "E!3fant3Gr1$"

    def __init__(self, longitud=None, password=None):
        self.longitud = longitud
        self.password = password

    def get_recomendation(self):
        return print(f"Recomendación: {self.__recomendation}")

    def set_recomendation(self, recomendation):
        self.__recomendation = recomendation
        return self.get_recomendation()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

    def esFuerte(self):
        mayusculas = sum(1 for c in self.password if c.isupper())
        minusculas = sum(1 for c in self.password if c.islower())
        numeros = sum(1 for c in self.password if c.isdigit())

        es_fuerte = (mayusculas > 2) and (minusculas > 1) and (numeros > 5)

        return print(f"Es fuerte: {es_fuerte}")

    def generarPassword(self):
        # Definir los caracteres posibles para la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation
        # Generar una contraseña de longitud específica
        contrasena = "".join(random.choice(caracteres) for _ in range(self.longitud))
        return print(f"Su contraseña generada es: {contrasena}")

    def seguridadPassword(self):
        longitud = len(self.password)
        contiene_letras = any(c.isalpha() for c in self.password)
        contiene_digitos = any(c.isdigit() for c in self.password)
        contiene_caracteres_especiales = any(
            c in string.punctuation for c in self.password
        )

        if longitud <= 6 and contiene_letras and contiene_digitos:
            return print("Seguridad: Débil")
        elif 7 <= longitud <= 10 and contiene_letras and contiene_digitos:
            return print("Seguridad: Media")
        elif (
            11 <= longitud <= 20
            and contiene_letras
            and contiene_digitos
            and contiene_caracteres_especiales
        ):
            return print("Seguridad: Fuerte")
        else:
            return print("No cumple con los criterios")


password_uno = Password(password="A1b2C@d3e4f")
password_uno.esFuerte()

print()

password_dos = Password(longitud=8)
password_dos.generarPassword()

print()

password_tres = Password(longitud=11, password="A1b2C@d3e4f")
password_tres.seguridadPassword()
password_tres.get_recomendation()
password_tres.set_recomendation("314235HU86")
password_tres.metodo_publico()
