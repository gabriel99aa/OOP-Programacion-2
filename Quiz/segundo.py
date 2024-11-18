# utilizando la estructura de datos pila agregar los siguientes elementos en el siguiente orden:

# pila = PilaStack()

# pila.enpilar({'name': 'A', 'age': 34, prioridad: 'Alta'})
# pila.enpilar({'name': 'B', 'age': 34, prioridad: 'Baja'})
# pila.enpilar({'name': 'C', 'age': 5, prioridad: 'Media'})
# pila.enpilar({'name': 'D', 'age': 77, prioridad: 'Baja'})
# pila.enpilar({'name': 'E', 'age': 55, prioridad: 'Media'})
# pila.enpilar({'name': 'F', 'age': 34, prioridad: 'Alta'})
# pila.enpilar({'name': 'G', 'age': 12, prioridad: 'Alta'})

# Realizar un metodo ver_pila_por_prioridad(prioridad) que se le ingrese la prioridad
# y muestre el nombre de los elementos con la prioridad selecionada
# en el orden de salida recomendada por la pila ejemplo:

# pila.ver_pila_por_prioridad('Alta')
# # G, F, A
# pila.ver_pila_por_prioridad('Media')
# # E, C
# pila.ver_pila_por_prioridad('Baja')
# D, B


class PilaStack:
    def __init__(self):
        self.elementos = []

    def enpilar(self, elemento):
        self.elementos.append(elemento)

    def desenpilar(self):
        if self.elementos:
            return self.elementos.pop()
        return None

    def ver_pila_por_prioridad(self, prioridad):
        solucion = []
        pila_temporal = self.elementos.copy()

        while pila_temporal:
            elemento = pila_temporal.pop()

            if elemento["prioridad"] == prioridad:
                solucion.append(elemento["name"])

        return print("solucion: ", solucion)


pila = PilaStack()

pila.enpilar({"name": "A", "age": 34, "prioridad": "Alta"})
pila.enpilar({"name": "B", "age": 34, "prioridad": "Baja"})
pila.enpilar({"name": "C", "age": 5, "prioridad": "Media"})
pila.enpilar({"name": "D", "age": 77, "prioridad": "Baja"})
pila.enpilar({"name": "E", "age": 55, "prioridad": "Media"})
pila.enpilar({"name": "F", "age": 34, "prioridad": "Alta"})
pila.enpilar({"name": "G", "age": 12, "prioridad": "Alta"})

print("enpilado: ", pila.elementos)

pila.ver_pila_por_prioridad("Alta")
pila.ver_pila_por_prioridad('Media')

pila.ver_pila_por_prioridad('Baja')