'''
사대의 수 m
동물의 수 n
사정거리 l
m개의 x 좌표값
'''
import sys
input = sys.stdin.readline

m, n, l = map(int, input().strip().split())
m_pos = list(map(int, input().strip().split()))
animal_pos = []

for _ in range(n):
    animal_pos.append(tuple(map(int, input().strip().split())))

m_pos.sort()
cnt = 0

def can_hunt(x, y):
    s = 0
    e = m - 1
    while s <= e:
        mid = (s + e) // 2
        if l >= (abs(m_pos[mid] - x) + y):
            return True
        if (x - y + l) >= m_pos[mid]:
            s = mid + 1
        else:
            e = mid - 1
        
    return False


for ani_x, ani_y in animal_pos:
    if can_hunt(ani_x, ani_y):
        cnt += 1

print(cnt)