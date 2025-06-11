from collections import deque
import sys


input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().strip().split())
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

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)