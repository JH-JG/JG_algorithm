import sys
input = sys.stdin.readline

n = int(input().strip())

tree = {}

for _ in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inoerder(root):
    if root != '.':
        inoerder(tree[root][0])
        print(root, end='')
        inoerder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inoerder('A')
print()
postorder('A')