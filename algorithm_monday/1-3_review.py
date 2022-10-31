import sys

input = sys.stdin.readline

arr = sorted(list(map(int, input().split())))

print(arr[3] + arr[2] - arr[1] - arr[0])
