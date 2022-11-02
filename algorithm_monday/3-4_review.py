import collections
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

graph = collections.defaultdict(list)
N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N + 1)]
circle = list()
found = -1


def findCycle(u, tar):
    global found

    if visited[u] == 1:
        found = u
        if u not in circle:
            circle.append(u)
        return

    visited[u] = 1

    for i in graph[u]:
        if i == tar:
            continue

        findCycle(i, u)

        if found == -2:
            return

        if found == u:
            found = -2
            return

        if found >= 0:
            if u not in circle:
                circle.append(u)
            return


findCycle(1, 1)

circle.sort()

print(len(circle))

for i in circle:
    print(i, end=' ')
