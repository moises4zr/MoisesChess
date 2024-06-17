from animal import Animal
from animal import Perro

#from animal import *   --- importa todas las clases del archivo animal.py 





def main():
    
    animal1 = Animal("Sunny","gato",4)
    animal2= Animal("Oreo", "gato", 3)
    
    
    print(f"animal:{animal1.nombre} , especie {animal1.especie} ")
    
    print(f"el nombre es {animal2.nombre}")
    
    
    print(animal1.moverse())
    
    print(animal2.moverse())
    
    
    
    
    
    perro1 = Perro("Didi", "perro",6 ,"Doberman")
    
    perro2 = Perro("Mario","perro", 5, "Aguacatero")
    
    
    print(perro1.nombre)
    print(perro1.raza)
    print(perro1.especie)
    
    print(f"el nombre es{perro1.nombre} y su raza es {perro1.raza} es de la especie {perro1.especie}")
    
    
    
    print(perro2.edad)
    
    
    
    
    
 
 
if __name__ == "__main__":
    main()
 
 
 