import random
import string


class Password:
    __recomendation = "E!3fant3Gr1$"

    def __init__(self, longitud=None, password=None):
        self.__longitud = longitud
        self.__password = password
        self.__min_mayusculas = 3
        self.__min_minusculas = 2
        self.__min_numeros = 5

    # Getters y Setters
    def get_longitud(self):
        return self.__longitud

    def set_longitud(self, longitud):
        self.__longitud = longitud

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_recomendation(self):
        return print(f"Recomendación: {self.__recomendation}")

    def set_recomendation(self, recomendation):
        self.__recomendation = recomendation
        return self.get_recomendation()

    def get_min_mayusculas(self):
        return self.__min_mayusculas

    def set_min_mayusculas(self, min_mayusculas):
        self.__min_mayusculas = min_mayusculas

    def get_min_minusculas(self):
        return self.__min_minusculas

    def set_min_minusculas(self, min_minusculas):
        self.__min_minusculas = min_minusculas

    def get_min_numeros(self):
        return self.__min_numeros

    def set_min_numeros(self, min_numeros):
        self.__min_numeros = min_numeros

    # Métodos privados
    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def __validar_longitud(self):
        return isinstance(self.__longitud, int) and self.__longitud > 0

    def __validar_password(self):
        return isinstance(self.__password, str) and len(self.__password) > 0

    def __contar_mayusculas(self):
        return sum(1 for c in self.__password if c.isupper())

    def __contar_minusculas(self):
        return sum(1 for c in self.__password if c.islower())

    def __contar_numeros(self):
        return sum(1 for c in self.__password if c.isdigit())

    # Método público que usa los métodos privados
    def metodo_publico(self):
        print(self.__metodo_privado())
        if self.__validar_longitud():
            print(f"Longitud válida: {self.__longitud}")
        else:
            print("Longitud no válida")

        if self.__validar_password():
            print(f"Password válido: {self.__password}")
        else:
            print("Password no válido")

        print(f"Número de mayúsculas: {self.__contar_mayusculas()}")
        print(f"Número de minúsculas: {self.__contar_minusculas()}")
        print(f"Número de números: {self.__contar_numeros()}")

    def esFuerte(self):
        mayusculas = self.__contar_mayusculas()
        minusculas = self.__contar_minusculas()
        numeros = self.__contar_numeros()

        es_fuerte = (
            (mayusculas >= self.__min_mayusculas)
            and (minusculas >= self.__min_minusculas)
            and (numeros >= self.__min_numeros)
        )

        return print(f"Es fuerte: {es_fuerte}")

    def generarPassword(self):
        # Definir los caracteres posibles para la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation
        # Generar una contraseña de longitud específica
        contrasena = "".join(random.choice(caracteres) for _ in range(self.__longitud))
        self.set_password(contrasena)  # Almacenar la contraseña generada
        return print(f"Su contraseña generada es: {contrasena}")

    def seguridadPassword(self):
        longitud = len(self.__password)
        contiene_letras = any(c.isalpha() for c in self.__password)
        contiene_digitos = any(c.isdigit() for c in self.__password)
        contiene_caracteres_especiales = any(
            c in string.punctuation for c in self.__password
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
password_uno.set_password("A1b2C@d3e4f")
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

print(password_tres.get_min_mayusculas())
password_tres.set_min_mayusculas(4)
print(password_tres.get_min_mayusculas())

print(password_tres.get_min_minusculas())
password_tres.set_min_minusculas(3)
print(password_tres.get_min_minusculas())

print(password_tres.get_min_numeros())
password_tres.set_min_numeros(6)
print(password_tres.get_min_numeros())
