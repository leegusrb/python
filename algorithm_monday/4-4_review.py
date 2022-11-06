import collections
import sys

input = sys.stdin.readline

n = int(input())
dp = collections.deque()

dp.append(0)
dp.append(0)
dp.append(1)

for i in range(3, n + 1):
    dp.append((2 * (i - 1) + 1) * dp[-1] + dp[-2])
    dp.popleft()

print(dp[-1] % 100000007)
