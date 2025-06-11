import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input().strip())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]


for _ in range(n-1):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(n):
    for i in graph[n]:
        if not visited[i]:
            visited[i] = n
            dfs(i)


dfs(1)

for i in range(2, n + 1):
    print(visited[i])