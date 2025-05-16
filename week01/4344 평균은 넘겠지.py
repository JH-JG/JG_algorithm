c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    n = scores[0]
    scores = scores[1:]

    avg = sum(scores) / n

    print(f'{round((sum([1 for score in scores if score > avg])/n)*100, 3)}%')