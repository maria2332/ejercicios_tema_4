import heapq

class Nodo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.vecinos = {}
    
    def agregar_vecino(self, vecino, peso=0):
        self.vecinos[vecino] = peso
    
    def __str__(self):
        return str(self.nombre) + ' ' + str(self.tipo) + ' vecinos: ' + str([x.nombre for x in self.vecinos])
    
    def __lt__(self, otro):
        return self.nombre < otro.nombre
        
class Estacion(Nodo):
    def __init__(self, nombre):
        super().__init__(nombre, 'estacion')
        
class Desvio(Nodo):
    contador = 0
    
    def __init__(self):
        Desvio.contador += 1
        super().__init__(Desvio.contador, 'desvio')

def dijkstra(grafo, inicio, fin):
    heap = [(0, inicio)]
    visitados = set()
    distancias = {inicio: 0}
    anteriores = {}
    
    while heap:
        (dist, actual) = heapq.heappop(heap)
        if actual in visitados:
            continue
        
        visitados.add(actual)
        
        if actual == fin:
            return distancias, anteriores
        
        for vecino in actual.vecinos:
            peso = actual.vecinos[vecino]
            if vecino in visitados:
                continue
            if vecino not in distancias or dist + peso < distancias[vecino]:
                distancias[vecino] = dist + peso
                anteriores[vecino] = actual
                heapq.heappush(heap, (distancias[vecino], vecino))
    
    return distancias, anteriores

# Crear el grafo
grafo = {}

# Agregar las estaciones de tren
estacion1 = Estacion('King\'s Cross')
estacion2 = Estacion('Waterloo')
estacion3 = Estacion('Victoria Train Station')
estacion4 = Estacion('Liverpool Street Station')
estacion5 = Estacion('St. Pancras')
estacion6 = Estacion('Euston')

grafo[estacion1.nombre] = estacion1
grafo[estacion2.nombre] = estacion2
grafo[estacion3.nombre] = estacion3
grafo[estacion4.nombre] = estacion4
grafo[estacion5.nombre] = estacion5
grafo[estacion6.nombre] = estacion6

# Agregar los desvíos
desvio1 = Desvio()
desvio2 = Desvio()
desvio3 = Desvio()
desvio4 = Desvio()
desvio5 = Desvio()
desvio6 = Desvio()

grafo[desvio1.nombre] = desvio1
grafo[desvio2.nombre] = desvio2
grafo[desvio3.nombre] = desvio3
grafo[desvio4.nombre] = desvio4
grafo[desvio5.nombre] = desvio5
grafo[desvio6.nombre] = desvio6


# Agregar las conexiones
estacion1.agregar_vecino(estacion2, 1)
estacion1.agregar_vecino(desvio1, 1)
estacion2.agregar_vecino(estacion1, 1)
estacion2.agregar_vecino(estacion3, 1)
estacion2.agregar_vecino(desvio2, 1)
estacion3.agregar_vecino(estacion2, 1)
estacion3.agregar_vecino(estacion4, 1)
estacion3.agregar_vecino(desvio3, 1)
estacion4.agregar_vecino(estacion3, 1)
estacion4.agregar_vecino(estacion5, 1)
estacion4.agregar_vecino(desvio4, 1)
estacion5.agregar_vecino(estacion4, 1)
estacion5.agregar_vecino(estacion6, 1)
estacion5.agregar_vecino(desvio5, 1)

estacion6.agregar_vecino(estacion5, 1)
estacion6.agregar_vecino(desvio6, 1)

desvio1.agregar_vecino(estacion1, 1)
desvio1.agregar_vecino(desvio2, 1)
desvio2.agregar_vecino(estacion2, 1)
desvio2.agregar_vecino(desvio1, 1)
desvio2.agregar_vecino(desvio3, 1)
desvio3.agregar_vecino(estacion3, 1)
desvio3.agregar_vecino(desvio2, 1)
desvio3.agregar_vecino(desvio4, 1)
desvio4.agregar_vecino(estacion4, 1)
desvio4.agregar_vecino(desvio3, 1)
desvio4.agregar_vecino(desvio5, 1)
desvio5.agregar_vecino(estacion5, 1)
desvio5.agregar_vecino(desvio4, 1)
desvio5.agregar_vecino(desvio6, 1)
desvio6.agregar_vecino(estacion6, 1)
desvio6.agregar_vecino(desvio5, 1)

# Calcular la ruta más corta
distancias, anteriores = dijkstra(grafo, estacion1, estacion6)

# Imprimir la ruta más corta

ruta = []
actual = estacion6
while actual:
    ruta.append(actual)
    actual = anteriores.get(actual, None)


print('La ruta más corta es: ' + str([x.nombre for x in ruta[::-1]]))
print('La distancia es: ' + str(distancias[estacion6]))

# La ruta más corta es: ['King\'s Cross', 1, 2, 3, 4, 5, 6]
# La distancia es: 6