width, height = map(int, input().split())

n = int(input())
w_cut = []
h_cut = []

for i in range(n):
    a, b = (map(int, input().split()))
    if a == 0:
        h_cut.append(b)
    else:
        w_cut.append(b)

h_cut.append(height)
w_cut.append(width)
h_cut.sort()
w_cut.sort()

h = [h_cut[0]]
w = [w_cut[0]]

for i in range(1, len(h_cut)):
    h.append(h_cut[i] - h_cut[i-1])
for i in range(1, len(w_cut)):
    w.append(w_cut[i] - w_cut[i-1])


print(max(h) * max(w))