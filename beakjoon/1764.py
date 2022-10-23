from sys import stdin

N, M = map(int, stdin.readline().split())

notListen = set()
notSee = set()
cnt = 0

for i in range(N):
    notListen.add(stdin.readline().strip())
for j in range(M):
    notSee.add(stdin.readline().strip())

notBoth = sorted(notListen & notSee)

print(len(notBoth))
for i in notBoth:
    print(i)
