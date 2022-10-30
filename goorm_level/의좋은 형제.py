from sys import stdin

N1, N2 = map(int, stdin.readline().split())
D = int(stdin.readline())

for i in range(D):
    if i % 2 == 1:
        N1 += (N2+1) // 2
        N2 -= (N2+1) // 2
    else:
        N2 += (N1+1) // 2
        N1 -= (N1+1) // 2

print(int(N1), int(N2))
