n = int(input())
n_list = list(map(int, input().split()))
n_dict = {x for x in n_list}

m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    if m_list[i] in n_dict:
        print(1)
    else:
        print(0)