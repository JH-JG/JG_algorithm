import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(n, group):
    visited[n] = group
    for i in graph[n]:
        if visited[i] == 0:
            if not dfs(i, -group):
                return False
        elif visited[n] == visited[i]:
            return False
    return True


K = int(input())

for _ in range(K):
    V, E = map(int, input().strip().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    
    for _ in range(E):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    is_bipartite = True

    for i in range(1, V + 1):
        if visited[i] == 0:
            if not dfs(i, 1):
                is_bipartite = False
                break
    
    print('YES' if is_bipartite else 'NO')