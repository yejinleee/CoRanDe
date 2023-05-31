import sys

def combination():
    for i in range(1, 31):
        for j in range(1, 31):
            if (i == j) or (j == 0):
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    
N = int(sys.stdin.readline())

arr = [[1 for j in range(31)] for i in range(31)]
combination()

for _ in range(N):
    n, r = map(int,sys.stdin.readline().split())
    print(arr[r][n])