import collections
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
Q = collections.deque()

for i in range(M):
    op, k = input().split()
    k = int(k)

    if op == 'deposit':
        N += k

        while Q and N >= Q[0]:
            N -= Q.popleft()
    elif op == 'pay':
        if N >= k:
            N -= k
    elif op == 'reservation':
        if N >= k and not Q:
            N -= k
        else:
            Q.append(k)

print(N)
