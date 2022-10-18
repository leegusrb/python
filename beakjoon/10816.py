from sys import stdin, stdout

N = int(stdin.readline())
A = sorted(list(map(int, stdin.readline().split())))
M = int(stdin.readline())
B = list(map(int, stdin.readline().split()))

def findElementNumber(A, left, right, e):
    if left > right:
        return 0
    mid = (left + right) // 2
    if e == A[mid]:
        return A[left:right + 1].count(e)
    elif e < A[mid]:
        return findElementNumber(A, left, mid - 1, e)
    else:
        return findElementNumber(A, mid + 1, right, e)

dic = {}

for e in B:
    if e not in dic:
        dic[e] = findElementNumber(A, 0, N - 1, e)

print(' '.join(str(dic[x]) if x in dic else '0' for x in B))

