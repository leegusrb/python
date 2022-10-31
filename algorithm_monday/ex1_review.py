import sys

input = sys.stdin.readline

n, k = map(int, input().split())

word = list()

for i in range(n):
    word.append(input().rstrip())

word.sort()
word.sort(key=lambda x: len(x))

print(word[k-1])
