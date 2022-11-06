st = input()

n = [0 for _ in range(4)]

for l in st:
    if l == '1':
        n[0] += 1
    elif l == 'I':
        n[1] += 1
    elif l == 'l':
        n[2] += 1
    elif l == '|':
        n[3] += 1

for i in n:
    print(i)
