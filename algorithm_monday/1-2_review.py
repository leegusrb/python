import sys

input = sys.stdin.readline

n, s = input().split()

cnt = 0
for i in range(int(n)):
    name = input()
    if s in name:
        cnt += 1

print(cnt)
