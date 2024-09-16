class Direccion:
    def __init__(self, calle, ciudad, código_postal, pais):
        self.calle = calle
        self.ciudad = ciudad
        self.código_postal = código_postal
        self.pais = pais
        
class Persona:
    def __init__(self, full_name, CC, direccion):
        self.full_name = full_name
        self.cc = CC
        self.direccion = direccion
        
class Estudiante(Persona):
    def __init__(self, id): 
        self.id = id
        
class Profesor(Persona):
    def __init__(self, oficina): 
        self.oficina = oficina