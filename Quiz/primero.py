# genera una clase celular que debe realizar lo siguiente:

# 1.⁠ ⁠nivel de carga
# 2.⁠ ⁠brillo de pantalla
# 3.⁠ ⁠atributo esta encendido
# 4.⁠ ⁠metodo cargar bateria el cual se le ingresa un parametro que varia de 1 a 100 y aumenta el nivel de carga
# 5.⁠ ⁠cuando el nivel de la bateria sea igual o mayor a 100 debe aparecer en cualquier metodo una alerta avisando por pantalla o imprimiendo que el celular esta cargado completamente sin importar si el celular esta apagado o encedido
# 6.⁠ ⁠si el celular esta encendido cada vez que se llame un metodo se debe llamar o invocar el metodo gasto de bateria que revisa el numero de 1 a 100 que tiene el brillo de la pantalla y este se dividira entre 10 y este resultado bajara el nivel de la bateria, nota si el nivel de la bateria es menor o igual a 1 el celular invocara el metodo apagar celular
# 7.⁠ ⁠crear metodo bajar intensidad de brillo de pantalla el cual se le ingresara un numero de 1 a 100 para configurar el brillo del celular
# 8.⁠ ⁠se debe crear un metodo apagar celular que bajara el brillo del celular a 0, nota mientras el celular esta apagado solo puede usarse 2 metodos(1. encender el celular, 2. cargar celular)
# 9.⁠ ⁠se debe crear un metodo encender celular que subira el brillo del celular a 30 y por lo tanto gastara bateria

class Celular:
    brillo = 0
    def __init__(self, encendido, carga= 0):
        self.encendido = encendido
        self.carga = carga
        
        
    def cargar_celular(self, nivel):
        self.carga += nivel
        if(self.carga >= 100):
            return print(f"su carga es: {self.carga} y su carga está completa")
        else:
            return print(f"su carga es: {self.carga}")
            
    def apagar_celular(self):
        if(self.encendido == True):
            self.brillo = 0
            self.encendido = False
            print(f"Apagado!!")
            if(self.carga >= 100):
                return print(f"Notificación: Su carga está completa!!")
            
    def encender_celular(self):
        if(self.encendido == False):
            self.encendido = True
            self.brillo = 30
            self.gasto_bateria()
            print(f"Encendido!!")
            if(self.carga >= 100):
                return print(f"Notificación: Su carga está completa!!")
    
    def gasto_bateria(self):
        if(self.encendido == True):
            print(f"gasto de batería: {self.carga - self.brillo / 10}")
            self.carga -= self.brillo / 10
            if(self.carga <= 1):
                self.apagar_celular()
        if(self.carga >= 100):
                return print(f"Notificación: Su carga está completa!!")
                
    def bajar_intemsidad(self, brillo):
        if(self.encendido == True):
            self.brillo = brillo
            print(f"brillo ajustado: {self.brillo}")
            if(self.carga >= 100):
                return print(f"Notificación: Su carga está completa!!")
            
iphone = Celular(True, 80)
iphone.cargar_celular(20)
iphone.apagar_celular()
iphone.encender_celular()
iphone.bajar_intemsidad(50)
