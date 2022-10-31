import sys

input = sys.stdin.readline

li = [0 for i in range(30)]

for i in range(28):
    li[int(input()) - 1] = 1

for i in range(30):
    if li[i] == 0:
        print(i + 1)
