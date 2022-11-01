import sys

input = sys.stdin.readline

N, k = map(int, input().split())

p = list()

for i in range(N):
    p.append(list(input().split()))

p.sort(key=lambda x: (x[0], x[1]))

print(p[k - 1][0], p[k - 1][1])
