import sys

N = int(sys.stdin.readline())

candy = [list(sys.stdin.readline().strip()) for _ in range(N)]

def check(arr, n):
    ans = 1
    
    for i in range(n):
        cnt = 1
        for j in range(1, n):  #행 확인
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

        cnt = 1
        for j in range(1, n): # 열 확인
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
    return ans

ans = 0
for i in range(N):
    for j in range(1, N):
        if candy[i][j] != candy[i][j-1]:
            candy[i][j] , candy[i][j-1] = candy[i][j-1], candy[i][j]
            ans = max(ans, check(candy, N))
            candy[i][j] , candy[i][j-1] = candy[i][j-1], candy[i][j]
        
        if candy[j][i] != candy[j-1][i]:
            candy[j][i] , candy[j-1][i] = candy[j-1][i], candy[j][i]
            ans = max(ans, check(candy, N))
            candy[j][i] , candy[j-1][i] = candy[j-1][i], candy[j][i]

print(ans)