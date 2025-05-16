n = int(input())

for i in range(n):
    quiz = input()
    score = 0
    answer = 1

    for q in quiz:
        if q == 'O':
            score += answer
            answer += 1
        else:
            answer = 1
    print(score)