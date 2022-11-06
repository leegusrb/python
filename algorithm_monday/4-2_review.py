import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
park = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    trees = list(map(int, input().split()))
    for j in range(N):
        park[i + 1][j + 1] = trees[j]

def isColored():
    global park, N
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if park[i][j]:
                return 0
    return 1

if isColored():
    print(0)
    exit(0)

update = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
day = 1

while 1:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if ni < 1 or nj < 1 or ni > N or nj > N:
                    continue
                if not park[ni][nj]:
                    update[i][j] += 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            park[i][j] = max(0, park[i][j] - update[i][j])

    if isColored():
        break

    day += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            update[i][j] = 0

print(day)
