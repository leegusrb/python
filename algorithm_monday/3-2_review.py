import sys

input = sys.stdin.readline

dic = {
    1: "1.,?!",
    2: "2ABC",
    3: "3DEF",
    4: "4GHI",
    5: "5JKL",
    6: "6MNO",
    7: "7PQRS",
    8: "8TUV",
    9: "9WXYZ"
}

n = int(input())
com = input()

ans = ""
cnt = 0
for i in range(n):
    if com[i] == com[i + 1]:
        cnt += 1
    else:
        cnt %= len(dic[int(com[i])])
        ans += dic[int(com[i])][cnt]
        cnt = 0

print(ans)
