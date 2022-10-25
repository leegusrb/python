from sys import stdin

N = int(stdin.readline())

people = sorted(list(map(int, stdin.readline().split())))

s = 0
for i in range(N):
    s += sum(people[:N-i])

print(s)
