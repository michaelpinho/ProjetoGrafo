class GrafoMatrizAdjacencia:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[0] * vertices for _ in range(vertices)]

    def adicionar_aresta(self, u, v):
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1


class GrafoListaAdjacencia:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista = {v: [] for v in range(vertices)}

    def adicionar_aresta(self, u, v):
        self.lista[u].append(v)
        self.lista[v].append(u)