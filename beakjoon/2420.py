from sys import stdin

N = sorted(list(map(int, stdin.readline().split())))

print(N[1] - N[0])


