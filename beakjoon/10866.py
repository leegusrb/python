from sys import stdin

N = int(stdin.readline())

def push_front(L, e):
    L.insert(0, e)

def push_back(L, e):
    L.append(e)

def size(L):
    return len(L)

def empty(L):
    if size(L) == 0:
        return 1
    else:
        return 0

def pop_front(L):
    if empty(L) == 1:
        return -1
    return L.pop(0)

def pop_back(L):
    if empty(L) == 1:
        return -1
    return L.pop(size(L) - 1)

def front(L):
    if empty(L) == 1:
        return -1

    return L[0]

def back(L):
    if empty(L) == 1:
        return -1

    return L[size(L) - 1]

L = []
for i in range(N):
    A = list(stdin.readline().split())
    if A[0] == 'push_front':
        push_front(L, A[1])
    elif A[0] == 'push_back':
        push_back(L, A[1])
    elif A[0] == 'pop_front':
        print(pop_front(L))
    elif A[0] == 'pop_back':
        print(pop_back(L))
    elif A[0] == 'size':
        print(size(L))
    elif A[0] == 'empty':
        print(empty(L))
    elif A[0] == 'front':
        print(front(L))
    elif A[0] == 'back':
        print(back(L))
