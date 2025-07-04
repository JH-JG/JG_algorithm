from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(n):
    print(n, end=' ')
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(i)


def bfs(n):
    visited[n] = True
    queue = deque([n])

    while queue:
        q = queue.popleft()
        print(q, end=' ')
        
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# 정점 번호가 작은 것이 먼저 오도록 정렬
for i in range(n + 1):
    graph[i].sort()

# 출력
visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)