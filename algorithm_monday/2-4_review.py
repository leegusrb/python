import collections
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

field = [[0 for _ in range(n)] for _ in range(n)]
Q = collections.deque()

for i in range(k):
    x, y = map(int, input().split())
    Q.append([x - 1, y - 1])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while Q:
    x, y = Q.pop()
    field[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            field[nx][ny] += 1

s = 0
for li in field:
    s += sum(li)

print(s)
