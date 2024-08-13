import random

class RobotExplorador:
    def __init__(self, laberinto, inicio):
        self.laberinto = laberinto
        self.posicion = inicio
        self.visitados = set()
        self.historial = []
        self.estado_actual = "explorando"
        self.direcciones = ["arriba", "abajo", "izquierda", "derecha"]

    def percepcion(self):
        x, y = self.posicion
        percepcion = {}

        if x > 0:
            percepcion["arriba"] = self.laberinto[x-1][y]
        if x < len(self.laberinto) - 1:
            percepcion["abajo"] = self.laberinto[x+1][y]
        if y > 0:
            percepcion["izquierda"] = self.laberinto[x][y-1]
        if y < len(self.laberinto[0]) - 1:
            percepcion["derecha"] = self.laberinto[x][y+1]

        return percepcion

    def mover(self, direccion):
        x, y = self.posicion
        if direccion == "arriba":
            self.posicion = (x-1, y)
        elif direccion == "abajo":
            self.posicion = (x+1, y)
        elif direccion == "izquierda":
            self.posicion = (x, y-1)
        elif direccion == "derecha":
            self.posicion = (x, y+1)
        self.historial.append(self.posicion)
        self.visitados.add(self.posicion)

    def retroceder(self):
        if len(self.historial) > 1:
            self.historial.pop()  # Eliminar la posición actual
            self.posicion = self.historial[-1]  # Volver a la anterior

    def decidir_accion(self, percepcion):
        acciones_posibles = []
        for direccion, estado in percepcion.items():
            nueva_posicion = self.calcular_nueva_posicion(direccion)
            if estado != 1 and nueva_posicion not in self.visitados:
                acciones_posibles.append(direccion)

        if acciones_posibles:
            return random.choice(acciones_posibles)
        else:
            return "retroceder"

    def calcular_nueva_posicion(self, direccion):
        x, y = self.posicion
        if direccion == "arriba":
            return (x-1, y)
        elif direccion == "abajo":
            return (x+1, y)
        elif direccion == "izquierda":
            return (x, y-1)
        elif direccion == "derecha":
            return (x, y+1)

    def explorar(self):
        while True:
            percepcion = self.percepcion()
            if self.laberinto[self.posicion[0]][self.posicion[1]] == 2:
                print(f"¡Salida encontrada en {self.posicion}!")
                break
            accion = self.decidir_accion(percepcion)
            if accion == "retroceder":
                print(f"Sin opciones, retrocediendo desde {self.posicion}")
                self.retroceder()
            else:
                print(f"Moviéndose {accion} desde {self.posicion}")
                self.mover(accion)

# Representación del laberinto: 0 = camino libre, 1 = obstáculo, 2 = salida
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 2],  # La salida está en la posición (3, 4)
    [0, 0, 1, 0, 0]
]

# Posición inicial del robot en (0, 0)
robot = RobotExplorador(laberinto, inicio=(0, 0))
robot.explorar()
