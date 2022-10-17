from sys import stdin

M, N = map(int, stdin.readline().split())

li = []

for i in range(M):
    li.append(stdin.readline().strip())

cntmin = M * N

for i in range(M - 7):
    for j in range(N - 7):
        cnt = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                    if li[x][y] == 'W':
                        cnt += 1
                else:
                    if li[x][y] == 'B':
                        cnt += 1
        cntmin = min(cntmin, (min(cnt, 8 * 8 - cnt)))
        
print(cntmin)
