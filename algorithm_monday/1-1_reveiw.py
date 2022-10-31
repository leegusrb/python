import sys

input = sys.stdin.readline

n = int(input())

B = list(map(int, input().split()))

ans = 1

for i in B:
    ans *= i

print(ans)
