def tsp(start, now, value, cnt):
    global cost
    # 모든 노드를 방문 후 다시 시작점으로
    if cnt == n:
        if a[now][start]:
            value += a[now][start]
            if cost > value:
                cost = value
        return
    
    # 도시로 가는 비용이 이미 가지고 있는 최소 값보다 크면 갈 이유 없음
    if value > cost:
        return
    
    for i in range(n):
        if not visited[i] and a[now][i]:
            visited[i] = True
            tsp(start, i, value + a[now][i], cnt + 1)
            visited[i] = False

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

cost = 100000000
visited = [0] * n

for i in range(n):
    visited[i] = True
    tsp(i, i, 0, 1) # 시작
    visited[i] = False

print(cost)
