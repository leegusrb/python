from sys import stdin

M, N = map(int, stdin.readline().split())

tomato = []

for i in range(N):
    tomato.append(list(map(int, stdin.readline().split())))

def tom(tomato):
    tmp = tomato
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if tmp[i] == 1:
                tomato[i + 1][j] = 1
                tomato[i][j + 1] = 1
                tomato[i - 1][j] = 1
                tomato[i][j - 1] = 1

