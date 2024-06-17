

class Animal:
    def __init__ (self, nombre, especie, edad):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
        
        
    def comer(self):
        return "el animal está comiendo"
    
    def moverse(self):
        return f"el {self.especie} se está moviendo"
    


class Perro(Animal):
    def __init__ (self, nombre, especie, edad, raza):
        super().__init__(nombre, especie,edad)
        self.raza=raza
        
        
        
    def comer(self):
        return f"{super().nombre} es un/a {super().especie} de raza {self.raza} y está comiendo"
    
    
    