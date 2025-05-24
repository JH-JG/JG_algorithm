import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    S = sys.stdin.readline().split()

    if S[0] == 'push':  # 정수 X를 큐에 넣는다.
        queue.append(int(S[1]))

    if S[0] == 'pop':   # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다
        if queue:   # Q 안에 값이 존재하는 경우
            print(queue.popleft())
        else:
            print(-1)

    if S[0] == 'size':  # 큐에 들어있는 정수의 개수를 출력한다.
        print(len(queue))

    if S[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')

    if S[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    if S[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)