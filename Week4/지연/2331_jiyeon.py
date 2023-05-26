import sys

def digitsum(num, p):
    n = [int(i)**p for i in str(num)]
    return sum(n)

A, P = map(int, sys.stdin.readline().split())
n = A
arr = [n]
idx = 0

while True:
    n = digitsum(n, P)
    if n not in arr:
        arr.append(n)
    else:
        idx = arr.index(n)
        break

print(idx)