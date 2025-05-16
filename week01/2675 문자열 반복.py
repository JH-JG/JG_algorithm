n = int(input())

for i in range(n):
    num, string = input().split()
    answer = ''
    for s in string:
        answer += (s * int(num))
    print(answer)