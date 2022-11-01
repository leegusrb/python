import collections
import sys

input = sys.stdin.readline
graph = collections.defaultdict(list)

N, M, K = map(int, input().split())

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1 for _ in range(N + 1)]
visited[1] = 0
q = collections.deque()
q.append(1)

while q:
    cur = q.popleft()
    for next in graph[cur]:
        if visited[next] != -1:
            continue
        q.append(next)
        visited[next] = visited[cur] + 1

if 1 <= visited[N] <= K:
    print("YES")
else:
    print("NO")
