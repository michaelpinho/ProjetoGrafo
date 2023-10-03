from collections import deque


class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.lista = [[] for _ in range(num_vertices)]

    def adc_aresta(self, u, v):
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1
        self.lista[u].append(v)
        self.lista[v].append(u)

    def imprimir_grafo(self):
        print("Matriz de Adjacência:")
        for row in self.matriz:
            print(row)

        print("\nLista de Adjacência:")
        for i, adj in enumerate(self.lista):
            print(f"{i+1}: {adj}")

    def bfs(self, source, target):
        dist = [-1] * self.num_vertices
        ant = [-1] * self.num_vertices
        isvisited = [False] * self.num_vertices
        q = deque()
        q.append(source)
        isvisited[source] = True
        dist[source] = 0

        while q:
            vertice_atual = q.popleft()

            if vertice_atual == target:
                break

            for vertice_vizinho in self.lista[vertice_atual]:
                if not isvisited[vertice_vizinho]:
                    dist[vertice_vizinho] = dist[vertice_atual] + 1
                    ant[vertice_vizinho] = vertice_atual
                    q.append(vertice_vizinho)
                    isvisited[vertice_vizinho] = True
        if dist[target] == -1 or ant[target] == -1:
            return None

        return dist, ant

    def dfs(self, source, target):
        visited = [False] * self.num_vertices
        pai = [-1] * self.num_vertices
        pilha = [source]

        while pilha:
            vertice_atual = pilha.pop()

            if vertice_atual == target:
                break

            if not visited[vertice_atual]:
                visited[vertice_atual] = True

                for vertice_vizinho in reversed(self.lista[vertice_atual]):
                    if not visited[vertice_vizinho]:
                        pai[vertice_vizinho] = vertice_atual
                        pilha.append(vertice_vizinho)

        if pai[target] == -1:
            return None

        return pai
