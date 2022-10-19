from sys import stdin

N = int(stdin.readline())

def pushL(L, e):
    L.append(e)

def sizeL(L):
    return len(L)

def emptyL(L):
    if sizeL(L) == 0:
        return 1
    else:
        return 0

def popL(L):
    if emptyL(L) == 1:
        return -1
    return L.pop(0)

def frontL(L):
    if emptyL(L) == 1:
        return -1

    return L[0]

def backL(L):
    if emptyL(L) == 1:
        return -1

    return L[sizeL(L) - 1]

L = []
for i in range(N):
    A = list(stdin.readline().split())
    if A[0] == 'push':
        pushL(L, A[1])
    elif A[0] == 'pop':
        print(popL(L))
    elif A[0] == 'size':
        print(sizeL(L))
    elif A[0] == 'empty':
        print(emptyL(L))
    elif A[0] == 'front':
        print(frontL(L))
    elif A[0] == 'back':
        print(backL(L))
