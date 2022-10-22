import copy
from sys import stdin

N, M, K = map(int, stdin.readline().split())

li = [[] for i in range(N + 1)]

for i in range(M):
    u, v = map(int, stdin.readline().split())
    li[u].append(v)
    li[v].append(u)


def count(li, back, island, N, cnt):
    if island == N:
        return cnt
    if cnt >= N:
        return N
    li2 = copy.deepcopy(li)
    if back != -1:
        li2[island].remove(back)
        li2[back].remove(island)
    if len(li2[island]) == 0:
        return N
    mini = N
    for i in li2[island]:
        mini = min(mini, count(li2, island, i, N, cnt + 1))
    return mini


c = count(li, -1, 1, N, 0)
if c <= K and c < N:
    print("YES")
else:
    print("NO")

# 6 6 2
# 1 4
# 4 2
# 2 6
# 4 3
# 1 2
# 3 1
#
# 6 6 2
# 1 2
# 2 3
# 3 4
# 3 5
# 5 6
# 5 2
#
# 3 1 1
# 1 2
