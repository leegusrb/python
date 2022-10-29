from sys import stdin

N = int(stdin.readline())
li = [0, 1, 2, 4]


def find_num(n):
    length = len(li)
    if n >= length:
        for i in range(length, n + 1):
            li.append(li[i - 3] + li[i - 2] + li[i - 1])
    print(li[n])


for i in range(N):
    n = int(stdin.readline())
    find_num(n)
