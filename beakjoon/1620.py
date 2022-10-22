import sys

N, M = map(int, sys.stdin.readline().split())

dic = {}

for i in range(1, N + 1):
    a = sys.stdin.readline().strip()
    dic[i] = a
    dic[a] = i

for i in range(M):
    find = sys.stdin.readline().strip()
    if find.isdigit():
        print(dic[int(find)])
    else:
        print(dic[find])
