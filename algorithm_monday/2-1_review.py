import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    avg = sum(v) / n
    cnt = 0
    for s in v:
        if s >= avg:
            cnt += 1
    print("%d/%d" %(cnt, n))
