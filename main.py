from grafo import Grafo


def load_from(filename):
    with open(filename, 'r') as f:
        num_vertices = int(f.readline().strip())
        g = Grafo(num_vertices)

        for i, line in enumerate(f):
            line = line.strip()
            num = line.split("\t")
            for j, valor in enumerate(num):
                g.matriz[i][j] = int(valor)
                if g.matriz[i][j] > 0:
                    g.lista[i].append(j)

    return g


if __name__ == "__main__":
    gr = load_from("grafonumeros.txt")
    gr.imprimir_grafo()
    source = 3
    target = 0
    print("BFS: ")
    dist, ant = gr.bfs(source, target)
    print("Distâncias: ", dist)
    print("Antecessores: ", ant)

    print("\nDFS:")
    dfs_pai = gr.dfs(source, target)
    print("Antecessores: ", dfs_pai)
