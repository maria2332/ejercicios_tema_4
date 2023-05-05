import heapq

class Estacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = "estacion"
    
class CambioDeAgujas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = "cambio de agujas"
    
class RedFerrocarriles:
    def __init__(self):
        self.grafo = {}
    
    def agregar_nodo(self, nodo):
        self.grafo[nodo.nombre] = []
    
    def agregar_arista(self, nodo1, nodo2):
        self.grafo[nodo1.nombre].append(nodo2.nombre)
        self.grafo[nodo2.nombre].append(nodo1.nombre)
    
    def calcular_camino_mas_corto(self, origen, destino):
        distancias = {}
        for nodo in self.grafo:
            distancias[nodo] = float("inf")
        distancias[origen] = 0
        heap = [(0, origen)]
        while heap:
            (dist, nodo_actual) = heapq.heappop(heap)
            if dist > distancias[nodo_actual]:
                continue
            for nodo_vecino in self.grafo[nodo_actual]:
                distancia_vecino = dist + 1
                if distancia_vecino < distancias[nodo_vecino]:
                    distancias[nodo_vecino] = distancia_vecino
                    heapq.heappush(heap, (distancia_vecino, nodo_vecino))
        return distancias[destino]

red = RedFerrocarriles()

# Estaciones
king_cross = Estacion("King's Cross")
waterloo = Estacion("Waterloo")
victoria = Estacion("Victoria Train Station")
liverpool_street = Estacion("Liverpool Street Station")
st_pancras = Estacion("St. Pancras")

red.agregar_nodo(king_cross)
red.agregar_nodo(waterloo)
red.agregar_nodo(victoria)
red.agregar_nodo(liverpool_street)
red.agregar_nodo(st_pancras)

red.agregar_arista(king_cross, st_pancras)
red.agregar_arista(king_cross, victoria)
red.agregar_arista(king_cross, liverpool_street)
red.agregar_arista(st_pancras, victoria)
red.agregar_arista(waterloo, victoria)
red.agregar_arista(waterloo, liverpool_street)
red.agregar_arista(liverpool_street, victoria)

print(red.calcular_camino_mas_corto(king_cross.nombre, waterloo.nombre))
print(red.calcular_camino_mas_corto(victoria.nombre, liverpool_street.nombre))
print(red.calcular_camino_mas_corto(st_pancras.nombre, king_cross.nombre))












# import heapq

# class Nodo:
#     def __init__(self, nombre, tipo):
#         self.nombre = nombre
#         self.tipo = tipo
#         self.vecinos = []
#         self.distancia = float('inf')
#         self.visitado = False
#         self.padre = None
    
#     def agregar_vecino(self, vecino, peso):
#         self.vecinos.append((vecino, peso))
    
#     def __lt__(self, otro):
#         return self.distancia < otro.distancia

# class Grafo:
#     def __init__(self):
#         self.nodos = {}
    
#     def agregar_nodo(self, nombre, tipo):
#         nodo = Nodo(nombre, tipo)
#         self.nodos[nombre] = nodo
#         return nodo
    
#     def agregar_arista(self, origen, destino, peso):
#         self.nodos[origen].agregar_vecino(self.nodos[destino], peso)
#         self.nodos[destino].agregar_vecino(self.nodos[origen], peso)
    
#     def dijkstra(self, origen, destino):
#         heap = []
#         self.nodos[origen].distancia = 0
#         heapq.heappush(heap, self.nodos[origen])
        
#         while heap:
#             actual = heapq.heappop(heap)
#             if actual.visitado:
#                 continue
#             actual.visitado = True
#             if actual.nombre == destino:
#                 break
            
#             for vecino, peso in actual.vecinos:
#                 nueva_distancia = actual.distancia + peso
#                 if nueva_distancia < vecino.distancia:
#                     vecino.distancia = nueva_distancia
#                     vecino.padre = actual
#                     heapq.heappush(heap, vecino)
        
#         camino = []
#         nodo_actual = self.nodos[destino]
#         while nodo_actual.padre is not None:
#             camino.append(nodo_actual.nombre)
#             nodo_actual = nodo_actual.padre
#         camino.append(origen)
#         camino.reverse()
        
#         return camino

# g = Grafo()

# # agregar estaciones
# g.agregar_nodo("King's Cross", "estacion")
# g.agregar_nodo("Waterloo", "estacion")
# g.agregar_nodo("Victoria Train Station", "estacion")
# g.agregar_nodo("Liverpool Street Station", "estacion")
# g.agregar_nodo("Paddington", "estacion")
# g.agregar_nodo("Marylebone", "estacion")

# # agregar desvios
# for i in range(1, 13):
#     g.agregar_nodo(str(i), "desvio")

# # agregar aristas
# g.agregar_arista("King's Cross", "1", 1)
# g.agregar_arista("King's Cross", "2", 1)
# g.agregar_arista("1", "2", 1)
# g.agregar_arista("1", "3", 1)
# g.agregar_arista("1", "4", 1)
# g.agregar_arista("2", "4", 1)
# g.agregar_arista("2", "5", 1)
# g.agregar_arista("3", "4", 1)
# g.agregar_arista("3", "6", 1)
# g.agregar_arista("4", "5", 1)
# g.agregar_arista("4", "6", 1)
# g.agregar_arista("4", "7", 1)
# g.agregar_arista("5", "7", 1)
# g.agregar_arista("5", "8", 1)
# g.agregar_arista("6", "7", 1)
# g.agregar_arista("6", "9", 1)
# g.agregar_arista("7", "8", 1)
# g.agregar_arista("7", "9", 1)
# g.agregar_arista("7", "10", 1)
# g.agregar_arista("8", "10", 1)
# g.agregar_arista("8", "11", 1)
# g.agregar_arista("9", "10", 1)
# g.agregar_arista("9", "12", 1)
# g.agregar_arista("10", "11", 1)
# g.agregar_arista("10", "12", 1)
# g.agregar_arista("11", "12", 1)
# g.agregar_arista("11", "Victoria Train Station", 1)
# g.agregar_arista("12", "Victoria Train Station", 1)
# g.agregar_arista("Victoria Train Station", "Liverpool Street Station", 1)
# g.agregar_arista("Victoria Train Station", "Paddington", 1)
# g.agregar_arista("Victoria Train Station", "Marylebone", 1)
# g.agregar_arista("Liverpool Street Station", "Paddington", 1)
# g.agregar_arista("Liverpool Street Station", "Marylebone", 1)
# g.agregar_arista("Paddington", "Marylebone", 1)

# # calcular camino
# camino = g.dijkstra("King's Cross", "Marylebone")
# print(camino)

# # calcular distancia
# distancia = 0
# for i in range(len(camino) - 1):
#     distancia += g.nodos[camino[i]].distancia
# print("La distancia es de:" ,distancia, "km")

# # calcular tiempo
# tiempo = distancia / 2
# print("El tiempo es de:" ,tiempo, "min")

# # calcular costo
# costo = 0
# for i in range(len(camino) - 1):
#     if g.nodos[camino[i]].tipo == "estacion":
#         costo += 2
#     else:
#         costo += 1
# print("El coste es de:" ,costo, "£")

# # calcular cantidad de desvios
# desvios = 0
# for i in range(len(camino) - 1):
#     if g.nodos[camino[i]].tipo == "desvio":
#         desvios += 1
# print("Ha tomado:" ,desvios, "desvios")

# # calcular cantidad de estaciones
# estaciones = 0
# for i in range(len(camino) - 1):
#     if g.nodos[camino[i]].tipo == "estacion":
#         estaciones += 1
# print("Ha tomado:" ,estaciones, "estaciones")

# # calcular cantidad de cruces
# cruces = 0
# for i in range(len(camino) - 1):
#     if g.nodos[camino[i]].tipo == "estacion" and g.nodos[camino[i + 1]].tipo == "estacion":
#         cruces += 1
# print("Ha tomado:" ,cruces, "cruces")

# # calcular cantidad de cambios de sentido
# cambios = 0
# for i in range(len(camino) - 1):
#     if g.nodos[camino[i]].tipo == "desvio" and g.nodos[camino[i + 1]].tipo == "desvio":
#         cambios += 1
# print("Ha tomado:" ,cambios, "cambios de sentido")

# # calcular cantidad de cambios de sentido en estaciones
# cambios_estaciones = 0
# for i in range(len(camino) - 1):
#     if g.nodos[camino[i]].tipo == "desvio" and g.nodos[camino[i + 1]].tipo == "desvio":
#         if g.nodos[camino[i - 1]].tipo == "estacion" and g.nodos[camino[i + 2]].tipo == "estacion":
#             cambios_estaciones += 1
# print("Ha tomado:" ,cambios_estaciones, "cambios de sentido en estaciones")

# # calcular cantidad de cambios de sentido en desvios
# cambios_desvios = 0
# for i in range(len(camino) - 1):
#     if g.nodos[camino[i]].tipo == "desvio" and g.nodos[camino[i + 1]].tipo == "desvio":
#         if g.nodos[camino[i - 1]].tipo == "desvio" and g.nodos[camino[i + 2]].tipo == "desvio":
#             cambios_desvios += 1
# print("Ha tomado:", cambios_desvios, "cambios de sentido en desvios")

# # calcular cantidad de cambios de sentido en estaciones y desvios
# cambios_mixtos = 0
# for i in range(len(camino) - 1):
#     if g.nodos[camino[i]].tipo == "desvio" and g.nodos[camino[i + 1]].tipo == "desvio":
#         if g.nodos[camino[i - 1]].tipo == "estacion" and g.nodos[camino[i + 2]].tipo == "desvio":
#             cambios_mixtos += 1
#         elif g.nodos[camino[i - 1]].tipo == "desvio" and g.nodos[camino[i + 2]].tipo == "estacion":
#             cambios_mixtos += 1
# print("Ha tomado:", cambios_mixtos, "cambios de sentido en estaciones y desvios")