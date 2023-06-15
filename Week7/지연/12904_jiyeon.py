import sys

S = list(sys.stdin.readline().strip())
T = list(sys.stdin.readline().strip())

while True:
    if len(T) == 0:
        print("0")
        break
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[::-1]
        T = T[1:]
    if T == S:
        print("1")
        break