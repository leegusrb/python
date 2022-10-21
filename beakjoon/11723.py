from sys import stdin

M = int(stdin.readline())
S = [0] * 20

def add(S, x):
    S[x - 1] = 1

def remove(S, x):
    S[x - 1] = 0

def check(S, x):
    if S[x - 1] == 1:
        return 1
    else:
        return 0

def toggle(S, x):
    if S[x - 1] == 1:
        S[x - 1] = 0
    else:
        S[x - 1] = 1

def all(S):
    for i in range(20):
        S[i] = 1

def empty(S):
    for i in range(20):
        S[i] = 0

for i in range(M):
    A = list(stdin.readline().split())

    if A[0] == 'add':
        add(S, int(A[1]))
    elif A[0] == 'remove':
        remove(S, int(A[1]))
    elif A[0] == 'check':
        print(check(S, int(A[1])))
    elif A[0] == 'toggle':
        toggle(S, int(A[1]))
    elif A[0] == 'all':
        all(S)
    elif A[0] == 'empty':
        empty(S)
