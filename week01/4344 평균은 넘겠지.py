c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    n = scores[0]
    scores = scores[1:]

    avg = sum(scores) / n

    print(f'{round((sum([1 for score in scores if score > avg])/n)*100, 3)}%')
'''
.3f로 처리해도 반올림을 해줌
'''