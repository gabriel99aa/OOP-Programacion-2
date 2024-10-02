from index import PilaStack

pila1 = PilaStack()

pila1.enpilar(2)
pila1.enpilar("MIKE")
pila1.enpilar(4)
pila1.enpilar("ROST")
pila1.enpilar(6)
pila1.enpilar("LILA")
pila1.enpilar(8)
pila1.enpilar("JUAN")
pila1.enpilar("PIPE")
pila1.enpilar(10)
print("respuesta ejercicio1 CASO 1: " + str(pila1.ejercicio1(5)))
# [2,'MIKE',4,'ROST',6,'LILA',8,'JUAN','PIPE',10,1,2,3,4,5]

pila2 = PilaStack()

pila2.enpilar(2)
pila2.enpilar("MIKE")
pila2.enpilar(1)
pila2.enpilar("ROST")
pila2.enpilar(2)
pila2.enpilar("LILA")
pila2.enpilar(3)
pila2.enpilar("JUAN")
pila2.enpilar("PIPE")
pila2.enpilar(10)
print("respuesta ejercicio1 CASO 2: " + str(pila2.ejercicio1(10)))
# [2,'MIKE',4,'ROST',6,'LILA',8,'JUAN','PIPE',10,1,2,3,4,5,6,7,8,9,10]
