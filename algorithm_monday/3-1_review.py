import collections
import sys

input = sys.stdin.readline

N = int(input())

p = list(map(int, input().split()))
dic = collections.defaultdict()

for i in p:
    if abs(i) in dic:
        dic.pop(abs(i))
    else:
        dic[i] = 1

print(sum(dic.keys()))
