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
