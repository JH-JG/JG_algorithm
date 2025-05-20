n = int(input())
li = []

for _ in range(n):
    li.append(input())

li = list(set(li))

li.sort(key=lambda x: (len(x), x))

for s in li:
    print(s)