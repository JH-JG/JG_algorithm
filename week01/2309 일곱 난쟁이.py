li = []

def dfs(n, start):
    if n == 7:
        if sum(short) == 100:
            for i in sorted(short):
                print(i)
            exit()
        else:
            return
    
    for i in range(start, len(li)):
        short.append(li[i])
        dfs(n+1, i+1)
        short.pop(-1)



for _ in range(9):
    li.append(int(input()))

short = []

dfs(0, 0)

'''
난쟁이가 중복으로 들어가지 않도록 조심

'''