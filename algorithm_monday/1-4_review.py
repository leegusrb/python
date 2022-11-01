import sys

input = sys.stdin.readline


def prime(n):
    check = [True] * (n + 1)

    m = int(n ** .5)
    for i in range(2, m + 1):
        if check[i]:
            for j in range(i + i, n + 1, i):
                check[j] = False

    return [i for i in range(2, n + 1) if check[i]]


N = int(input())
p = prime(N)

A = list(map(int, input().split()))
result = 0

for i in p:
    result += A[i - 1]

print(result)
