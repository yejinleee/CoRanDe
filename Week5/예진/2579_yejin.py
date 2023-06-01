#계단 오르기    ##참고
import sys
input = sys.stdin.readline

n = int(input())
p = [int(input()) for _ in range(n)]
if n<3:
    print(sum(p))
else:
    dp = [ p[0], p[0]+ p[1], max(p[0]+p[2], p[1]+p[2])]
    for i in range(3,n):
        dp.append(max( dp[i-2]+p[i] , dp[i-3]+p[i-1]+p[i]))
    print(dp[-1])

'''
i=3부터
ㅇㅇxㅇ(본) 이 클지, ㅇxㅇㅇ(본) 이 클지
두개전꺼까지 최대라고 구해놓은거 + 본인p값     vs   세개전꺼까지 최대라고 구해놓은거 + p[i-1]+p[i]

i == n 에서도 똑같넴
'''

'''겠냐 ..
tot = point[0]
cnt = 1
for i in range(1,n):
    if cnt ==1 :
        if i == n-2:
            if point[i] > point[n-3]:
                tot -= point[n-3]
                tot +=point[i]
                cnt =1
            else:
                cnt =0
        else:
            tot +=point[i]
            cnt+=1
    elif cnt ==2 :
        if point[i] > point[i-1]:
            tot -= point[i-1]
            tot += point[i]
            cnt =1
        else:
            cnt =0
    elif cnt ==0:
        tot +=point[i]
        cnt+=1
print(tot)
'''
