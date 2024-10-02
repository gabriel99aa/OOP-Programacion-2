from index import PilaStack

pila2 = PilaStack()

pila2.enpilar(2)
pila2.enpilar("MIKE")
pila2.enpilar(4)
pila2.enpilar("ROST")
pila2.enpilar(6)
pila2.enpilar("LILA")
pila2.enpilar(8)
pila2.enpilar("JUAN")
pila2.enpilar("PIPE")
pila2.enpilar(10)

print(pila2.ejercicio2())

pila3 = PilaStack()

pila3.enpilar(2)
# pila3.enpilar("MIKE")
pila3.enpilar(1)
# pila3.enpilar("ROST")
pila3.enpilar(2)
# pila3.enpilar("LILA")
pila3.enpilar(3)
# pila3.enpilar("JUAN")
# pila3.enpilar("PIPE")
pila3.enpilar(10)

print(pila3.ejercicio2())
