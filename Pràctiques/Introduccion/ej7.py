from typing import *

class Estudiante:
    def __init__(self, nombre):
        self.nombre=nombre
        self.notas={}

    def califica(self, asigantura, nota):
        self.notas[asigantura]=nota

    def nota(self, asinatura):
        return self.notas[asinatura]

    def media(self):
        suma=0
        num_asig=0
        for asig in self.notas:
            suma+=self.notas[asig]
            num_asig+=1
        return suma/num_asig

    def muestra_expediente(self):
        print(self.nombre)
        for asig in self.notas:
            print(f"{asig}: {self.notas[asig]}")

e=Estudiante("David")
e.califica('EI1022', 10)
e.califica('EI1023', 8)
e.nota('EI1022')
print(e.media())
e.muestra_expediente()
