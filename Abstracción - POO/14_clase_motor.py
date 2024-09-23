class Motor:
    def __init__(self):
        self.__consumo_litros = 0.0  # Atributo privado
        self.__encendido = False  # Atributo privado
        self.__marcha = 1  # Atributo privado
        self.__rpm = 0  # Atributo privado
        self.__siniestrado = False  # Atributo privado

    def get_siniestrado(self):
        return print(f"Siniestrado: {self.__siniestrado}")

    def set_siniestrado(self, siniestrado):
        self.__siniestrado = siniestrado
        return self.get_siniestrado()

    def get_consumo_litros(self):
        return self.__consumo_litros

    def set_consumo_litros(self, consumo):
        self.__consumo_litros = consumo

    def get_encendido(self):
        return self.__encendido

    def set_encendido(self, encendido):
        self.__encendido = encendido

    def get_marcha(self):
        return self.__marcha

    def set_marcha(self, marcha):
        self.__marcha = marcha

    def get_rpm(self):
        return self.__rpm

    def set_rpm(self, rpm):
        self.__rpm = rpm

    def __metodo_privado(self):
        return "DENTRO DEL MÉTODO PRIVADO"

    def __calcular_consumo(self):
        return self.__consumo_litros

    def __verificar_estado_motor(self):
        return self.__encendido

    def __ajustar_rpm(self, rpm):
        self.__rpm = rpm

    def __actualizar_consumo(self, consumo):
        self.__consumo_litros += consumo

    def metodo_publico(self):
        estado_motor = "Encendido" if self.__verificar_estado_motor() else "Apagado"
        consumo = self.__calcular_consumo()
        print(
            f"{self.__metodo_privado()} | Estado del motor: {estado_motor} | Consumo total: {consumo} L"
        )

    def arrancar(self):
        if not self.__encendido:
            self.__encendido = True
            self.__marcha = 1
            self.__rpm = 500
            print(f"Marcha: {self.__marcha} - RPM: {self.__rpm}")
        else:
            print("⚡️ Va a dañar el arranque!! ⚡️")

    def subir_cambio(self):
        if self.__marcha < 5:
            self.__marcha += 1
            print(f"Nueva marcha: {self.__marcha}")
        else:
            print("Error: R de rapidísimo")

    def bajar_cambio(self):
        if self.__marcha > 1:
            self.__marcha -= 1
            print(f"Nueva marcha: {self.__marcha}")
        else:
            print("Error: Está en reversa")

    def error_manager(self, rpm, tipo):
        if rpm > 5000:
            print("Error: El motor solo soporta 5000 rpm 💥")
        elif rpm < 0:
            print("Error: El motor no puede tener rpm negativas")
        elif rpm == 0:
            self.__encendido = False
            print("Se apagó el motor 🚙💤")
        elif rpm < self.__rpm and tipo == "aumentar":
            print(
                f"Error: Este método es para aumentar las rpm, rpm actual: {self.__rpm}"
            )
        elif rpm > self.__rpm and tipo == "disminuir":
            print(
                f"Error: Este método es para disminuir las rpm, rpm actual: {self.__rpm}"
            )

    def subir_rpm(self, rpm):
        if self.__encendido:
            if 0 < rpm <= 5000 and rpm > self.__rpm:
                self.__ajustar_rpm(rpm)
                print(f"Nuevo valor de rpm: {self.__rpm}")
            else:
                self.error_manager(rpm, tipo="aumentar")
        else:
            print("Error: No puede subir las rpm con el motor apagado")

    def bajar_rpm(self, rpm):
        if self.__encendido:
            if 0 < rpm <= 5000 and rpm < self.__rpm:
                self.__ajustar_rpm(rpm)
                print(f"Nuevo valor de rpm: {self.__rpm}")
            else:
                self.error_manager(rpm, tipo="disminuir")
        else:
            print("Error: No puede bajar las rpm con el motor apagado")

    def velocidad(self):
        calculo_velocidad = (self.__rpm / 100) * (0.5 + (self.__marcha / 2))
        print(f"Su velocidad es: {calculo_velocidad} Km/h")

    def consumo_por_marcha(self, consumo_por_rpm):
        if self.__marcha == 1:
            print("La marcha es Primera, se multiplica por 3")
            return consumo_por_rpm * 3
        elif self.__marcha == 2:
            print("La marcha es Segunda, se multiplica por 2")
            return consumo_por_rpm * 2
        else:
            print(f"La marcha es {self.__marcha}, no se multiplica el consumo")
            return consumo_por_rpm

    def consumo_actual_por_km(self):
        consumo_base = 0.05
        if self.__encendido:
            if self.__rpm <= 3000:
                self.__actualizar_consumo(self.consumo_por_marcha(0.05))
                print(f"Su consumo es: {self.__consumo_litros} L/km")

            elif 3000 < self.__rpm <= 3500:
                calculo_consumo_1 = (self.__rpm - 2500) / 500
                self.__actualizar_consumo(
                    self.consumo_por_marcha(consumo_base * calculo_consumo_1)
                )
                print(f"Su consumo es: {self.__consumo_litros} L/km")

            elif 3500 < self.__rpm <= 4000:
                calculo_consumo_2 = consumo_base * 2
                self.__actualizar_consumo(self.consumo_por_marcha(calculo_consumo_2))
                print(f"Su consumo es: {self.__consumo_litros} L/km")

            elif 4000 < self.__rpm <= 4500:
                calculo_consumo_3 = consumo_base * 3
                self.__actualizar_consumo(self.consumo_por_marcha(calculo_consumo_3))
                print(f"Su consumo es: {self.__consumo_litros} L/km")

            elif 4500 < self.__rpm < 5000:
                calculo_consumo_4 = consumo_base * 4
                self.__actualizar_consumo(self.consumo_por_marcha(calculo_consumo_4))
                print(f"Su consumo es: {self.__consumo_litros} L/km")

            elif self.__rpm == 5000:
                calculo_consumo_5 = consumo_base * 5
                self.__actualizar_consumo(self.consumo_por_marcha(calculo_consumo_5))
                print(f"Su consumo es: {self.__consumo_litros} L/km")
        else:
            print("Error: No puede calcular el consumo con el motor apagado")


# Ejemplo de uso
motor_1 = Motor()
motor_1.arrancar()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.subir_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.subir_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.subir_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.subir_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.subir_cambio()
print("------------------------------------------------")
motor_1.bajar_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.bajar_cambio()
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.subir_rpm(4000)
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.subir_rpm(5000)
motor_1.consumo_actual_por_km()
motor_1.velocidad()
print("------------------------------------------------")
motor_1.subir_rpm(5500)
print("------------------------------------------------")

motor_1.get_siniestrado()
motor_1.set_siniestrado(True)
motor_1.metodo_publico()
