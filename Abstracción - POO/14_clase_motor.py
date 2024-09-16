# motor tiene 5 cambios
# soporta hasta 5000 RPM
# La velocidad del auto se calcula así: (rpm / 100) * (0.5 + (cambio / 2))
# controlar el consumo. Se parte de una base de 0.05 litros por kilómetro
# Si el motor está a más de 3000 rpm, entonces se multiplica por (rpm - 2500) / 500.

# 14. Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos
# piden hacer un metodo constructor concentrado en las características del motor. El prototipo
# de motor tiene 5 cambios (de primera a quinta), y soporta hasta 5000 RPM.
# La velocidad del auto se calcula así: (rpm / 100) * (0.5 + (cambio / 2)). P.ej. en
# tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40.
# También nos interesa controlar el consumo. Se parte de una base de 0.05 litros por
# kilómetro. A este valor se le aplican los siguientes ajustes:
# Si el motor está a más de 3000 rpm, entonces se multiplica por
# (rpm - 2500) / 500.
# P.ej., a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
# Si el motor está en primera, entonces se multiplica por 3.
# Si el motor está en segunda, entonces se multiplica por 2.
# Los efectos por revoluciones y por cambio se acumulan. P.ej. si el motor está en
# primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km.

# El metodo constructor debe entender estos mensajes:
# arrancar(), se pone en primera con 500 rpm.
# subirCambio()
# bajarCambio()
# subirRPM(cuantos)
# bajarRPM(cuantos)
# velocidad()
# consumoActualPorKm()


class Motor:
    consumo_litros = 0.0
    encendido = False
    marcha = 1
    rpm = 0
    __siniestrado = False

    def get_siniestrado(self):
        return print(f"Siniestrado: {self.__siniestrado}")

    def set_siniestrado(self, siniestrado):
        self.__siniestrado = siniestrado
        return self.get_siniestrado()

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def metodo_publico(self):
        return print(f"{self.__metodo_privado()}")

    def arrancar(self):
        if self.encendido == False:
            self.encendido = True
            self.marcha = 1
            self.rpm = 500
            return print(f"Marcha: {self.marcha} - RPM: {self.rpm}")
        else:
            return print("⚡️ Va a dañar el arranque!! ⚡️")

    def subir_cambio(self):
        if self.marcha < 5:
            self.marcha += 1
            return print(f"Nueva marcha: {self.marcha}")
        else:
            return print("Error: R de rapidísimo")

    def bajar_cambio(self):
        if self.marcha > 1:
            self.marcha -= 1
            return print(f"Nueva marcha: {self.marcha}")
        else:
            return print("Error: Está en reversa")

    def error_manager(self, rpm, type):
        if rpm > 5000:
            return print("Error: El motor solo soporta 5000 rpm 💥")
        if rpm < 0:
            return print("Error: El motor no puede tener rpm negativas")
        if rpm == 0:
            self.encendido == False
            return print("Se apagó el motor 🚙💤")
        if rpm < self.rpm and type == "aumentar":
            return print(
                f"Error: Este método es para aumentar las rpm, rpm actual: {self.rpm}"
            )
        elif rpm > self.rpm and type == "disminuir":
            return print(
                f"Error: Este método es para disminuir las rpm, rpm actual: {self.rpm}"
            )

    def subir_rpm(self, rpm):
        if self.encendido:
            if rpm <= 5000 and rpm > 0 and rpm > self.rpm:
                self.rpm = rpm
                return print(f"Nuevo valor de rpm: {self.rpm}")
            else:
                self.error_manager(rpm, type="aumentar")
        else:
            return print("Error: No puede subir las rpm con el motor apagado")

    def bajar_rpm(self, rpm):
        if self.encendido:
            if rpm <= 5000 and rpm > 0 and rpm > self.rpm:
                self.rpm = rpm
                return print(f"Nuevo valor de rpm: {self.rpm}")
            else:
                self.error_manager(rpm, type="disminuir")
        else:
            return print("Error: No puede bajar las rpm con el motor apagado")

    def velocidad(self):
        calculo_velocidad = (self.rpm / 100) * (0.5 + (self.marcha / 2))
        return print(f"Su velocidad es: {calculo_velocidad} Km/h")

    def consumo_por_marcha(self, consumo_por_rpm):
        if self.marcha == 1:
            print("La marcha es Primera, se multiplica por 3")
            return consumo_por_rpm * 3
        elif self.marcha == 2:
            print("La marcha es Segunda, se multiplica por 2")
            return consumo_por_rpm * 2
        else:
            print(f"La marcha es {self.marcha}, no se multiplica el consumo")
            return consumo_por_rpm

    def consumo_actual_por_km(self):
        consumo_base = 0.05
        if self.encendido:
            if self.rpm <= 3000:
                self.consumo_litros += self.consumo_por_marcha(0.05)
                return print(f"Su consumo es: {self.consumo_litros} L/km")

            if self.rpm > 3000 and self.rpm <= 3500:
                calculo_consumo_1 = (self.rpm - 2500) / 500
                self.consumo_litros += self.consumo_por_marcha(
                    consumo_base * calculo_consumo_1
                )
                return print(f"Su consumo es: {self.consumo_litros} L/km")

            if self.rpm > 3500 and self.rpm <= 4000:
                calculo_consumo_2 = consumo_base * 2
                self.consumo_litros += self.consumo_por_marcha(calculo_consumo_2)
                return print(f"Su consumo es: {self.consumo_litros} L/km")

            if self.rpm > 4000 and self.rpm <= 4500:
                calculo_consumo_3 = consumo_base * 3
                self.consumo_litros += self.consumo_por_marcha(calculo_consumo_3)
                return print(f"Su consumo es: {self.consumo_litros} L/km")

            if self.rpm > 4500 and self.rpm < 5000:
                calculo_consumo_4 = consumo_base * 4
                self.consumo_litros += self.consumo_por_marcha(calculo_consumo_4)
                return print(f"Su consumo es: {self.consumo_litros} L/km")

            if self.rpm == 5000:
                calculo_consumo_5 = consumo_base * 5
                self.consumo_litros += self.consumo_por_marcha(calculo_consumo_5)
                return print(f"Su consumo es: {self.consumo_litros} L/km")
        else:
            return print("Error: No puede bajar las rpm con el motor apagado")


motor_1 = Motor()
motor_1.arrancar()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos a subimos a segunda 👇🏻
motor_1.subir_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos a subimos a tercera 👇🏻
motor_1.subir_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos a subimos a cuarta 👇🏻
motor_1.subir_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos a subimos a quinta 👇🏻
motor_1.subir_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos a causar un error por subimos de marcha 👇🏻
motor_1.subir_cambio()
print("------------------------------------------------")
# Vamos a disminuir de marcha a cuarta 👇🏻
motor_1.bajar_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos a disminuir de marcha a tercera 👇🏻
motor_1.bajar_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos a subir RPM 👇🏻
motor_1.subir_rpm(4000)
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos a subir RPM 👇🏻
motor_1.subir_rpm(5000)
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
# Vamos causar un error por subimos RPM 👇🏻
motor_1.subir_rpm(5500)
print("------------------------------------------------")

motor_1.get_siniestrado()
motor_1.set_siniestrado(True)
motor_1.metodo_publico()
