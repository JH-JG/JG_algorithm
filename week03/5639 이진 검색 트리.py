import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

def post(left, right):
    if left > right:
        return
    mid = right + 1
    for i in range(left + 1, right + 1):
        if pre[i] > pre[left]:
            mid = i
            break
    post(left + 1, mid - 1) #왼쪽 트리
    post(mid, right) #오른쪽 트리
    print(pre[left]) #루트 노드

post(0, len(pre) - 1)