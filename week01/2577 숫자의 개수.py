a = int(input())
b = int(input())
c = int(input())

num= {'0': 0,'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0}

mul = str(a * b * c)

for n in mul:
    num[n] += 1

for i in num.values():
    print(i)