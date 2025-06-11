n = int(input())

meets = []

for _ in range(n):
    s, e = map(int, input().split())
    meets.append((s, e))

meets.sort(key=lambda x: (x[1], x[0]))

cur_end = 0
cnt = 0

for s, e in meets:
    if cur_end <= s:
        cnt += 1
        cur_end = e

print(cnt)