from sys import stdin

li = []


def deposit(account, k):
    account += k
    return account


def pay(account, k):
    if account >= k:
        account -= k
    return account


def reservation(account, k):
    if account < k or len(li) != 0:
        li.append(k)
    else:
        account -= k
    return account


def update(account):
    while len(li) != 0 and li[0] <= account:
        account -= li.pop(0)
    return account


N, M = map(int, stdin.readline().split())

for i in range(M):
    a = list(stdin.readline().split())
    if a[0] == 'deposit':
        N = deposit(N, int(a[1]))
    elif a[0] == 'pay':
        N = pay(N, int(a[1]))
    elif a[0] == 'reservation':
        N = reservation(N, int(a[1]))
    N = update(N)


print(N)

