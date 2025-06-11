import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())
a = input()

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(n, visited, a):
    indoor_count = 0
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            if a[i - 1] == '1':
                indoor_count += 1
            else:
                indoor_count += dfs(i, visited, a)
    return indoor_count

answer = 0

# 실내 끼리 인접
for i in range(1, n + 1):
    if a[i - 1] == '1':
        for j in graph[i]:
            if a[j-1] == '1':
                answer += 1

# 실외-실내
for i in range(1, n + 1):
    if a[i - 1] == '0' and not visited[i]:
        indoor_count = dfs(i, visited, a)
        answer += indoor_count * (indoor_count - 1)

print(answer)