import sys
from collections import deque


def dfs(g, v, visited):
    visited[v] = True
    print(v, end=' ')

    for node in g[v]:
        if not visited[node]:
            dfs(g, node, visited)


def bfs(g, v, visited):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()

        if not visited[v]:
            visited[v] = True
            print(v, end=' ')

            for node in g[v]:
                if not visited[node]:
                    queue.append(node)


if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, V = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for i in range(M):
        edge = list(map(int, input().split()))

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    for g in graph:
        if g:
            g.sort()

    dfs(graph, V, [False] * (N + 1))
    print()
    bfs(graph, V, [False] * (N + 1))
