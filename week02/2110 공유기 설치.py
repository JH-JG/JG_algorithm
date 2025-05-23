import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

start = 1 # 최소 거리
end = home[-1] - home[0] # 최대 거리
result = 0

while start <= end:
    cnt = 1 # 가장 처음 집은 무조건 방문
    mid = (start + end) // 2
    last = home[0] # 마지막 설치한 집, 반복이 끝나면 다시 초기화

    for i in range(1, n):
        # 현재 집과 마지막 방문한 집에 거리 차이가 mid 보다 커야 i번째 집 설치
        # 설치를 했다면 cnt 증가, 마지막 방문한 집 교체
        if home[i] - last >= mid:
            cnt += 1
            last = home[i]
        
    # 집을 많이 방문했다면 mid를 늘려서 돌려봄, 거리 증가
    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
