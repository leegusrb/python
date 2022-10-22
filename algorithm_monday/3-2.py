from sys import stdin

n = int(stdin.readline())

s = stdin.readline()

def change(num, cnt):
    count = cnt % 5 + 1 if num == 1 or num == 7 or num == 9 else cnt % 4 + 1
    if num == 1:
        if count == 1:
            return '1'
        if count == 2:
            return '.'
        if count == 3:
            return ','
        if count == 4:
            return '?'
        else:
            return '!'
    if num == 2:
        if count == 1:
            return '2'
        if count == 2:
            return 'A'
        if count == 3:
            return 'B'
        else:
            return 'C'
    if num == 3:
        if count == 1:
            return '3'
        if count == 2:
            return 'D'
        if count == 3:
            return 'E'
        else:
            return 'F'
    if num == 4:
        if count == 1:
            return '4'
        if count == 2:
            return 'G'
        if count == 3:
            return 'H'
        else:
            return 'I'
    if num == 5:
        if count == 1:
            return '5'
        if count == 2:
            return 'J'
        if count == 3:
            return 'K'
        else:
            return 'L'
    if num == 6:
        if count == 1:
            return '6'
        if count == 2:
            return 'M'
        if count == 3:
            return 'N'
        else:
            return 'O'
    if num == 7:
        if count == 1:
            return '7'
        if count == 2:
            return 'P'
        if count == 3:
            return 'Q'
        if count == 4:
            return 'R'
        else:
            return 'S'
    if num == 8:
        if count == 1:
            return '8'
        if count == 2:
            return 'T'
        if count == 3:
            return 'U'
        else:
            return 'V'
    else:
        if count == 1:
            return '9'
        if count == 2:
            return 'W'
        if count == 3:
            return 'X'
        if count == 4:
            return 'Y'
        else:
            return 'Z'

chk = '0'
cnt = 0
str = ''

for num in s:
    if chk != num:
        if chk != '0':
            str += change(int(chk), cnt)
        chk = num
        cnt = 0
    else:
        cnt += 1

print(str)
