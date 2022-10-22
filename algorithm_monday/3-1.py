from sys import stdin

N = int(stdin.readline())

p = list(map(int, stdin.readline().split()))

score = sum(p)

print(score)
