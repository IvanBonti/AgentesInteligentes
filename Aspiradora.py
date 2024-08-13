import random

class Aspiradora:
    def __init__(self):
        self.posicion = "A"
        self.estado_A = "Sucio"
        self.estado_B = "Sucio"

    def Aspirar(self):
        if self.posicion == "A":
            self.estado_A = "Limpio"
            print("Se aspiró la posición A")
        else:
            self.estado_B = "Limpio"
            print("Se aspiró la posición B")

    def Derecha(self):
        self.posicion = "B"
        print("Se movió a la posición B")

    def Izquierda(self):
        self.posicion = "A"
        print("Se movió a la posición A")

    def Ensuciar(self):
        if random.choice(['A', 'B']) == 'A':
            self.estado_A = "Sucio"
            print("La posición A se ensució")
        else:
            self.estado_B = "Sucio"
            print("La posición B se ensució")

    def Operar(self, ciclos):
        for _ in range(ciclos):
            self.Ensuciar()
            if self.posicion == "A" and self.estado_A == "Sucio":
                self.Aspirar()
                self.Derecha()
            elif self.posicion == "B" and self.estado_B == "Sucio":
                self.Aspirar()
                self.Izquierda()
            else:
                if self.posicion == "A":
                    self.Derecha()
                else:
                    self.Izquierda()
            print("-" * 30)

asp = Aspiradora()
asp.Operar(5)
