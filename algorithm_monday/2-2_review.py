import sys

input = sys.stdin.readline

N = int(input())

s = input()

cnt = 1
for i in range(0, N - 1):
    if s[i] != s[i + 1]:
        cnt += 1

print(cnt)
