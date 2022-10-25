from sys import stdin

T = int(stdin.readline())

zero = [1, 0, 1]
one = [0, 1, 1]


def fiboonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[num], one[num])


for i in range(T):
    N = int(stdin.readline())
    a = [0, 0]
    fiboonacci(N)
