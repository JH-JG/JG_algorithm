from collections import deque
v = int(input())

n = int(input())

graph = [[] for _ in range(v + 1)]
visited = [False for _ in range(v+1)]

for i in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(n):
    visited[n] = True
    queue = deque([n])

    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(1)
print(sum(visited) - 1)