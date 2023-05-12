# 24. 회의실배정(실1) 맞음

import sys
input = sys.stdin.readline

N = int(input())
C = []
for i in range (N) :
  C.append(list(map(int, input().split())))

C.sort(key = lambda x: (x[1] , x[0])) #1.끝난 시간 2.시작 시간 기분으로 정렬

end = C[0][1]
result = 1

for i in range (1, N) :
  if C[i][0] >= end : #시작시간이 앞에 끝난 시간 보다 크거나 같으면
    result += 1 #result 값 올려주고
    end = C[i][1] # 끝난 시간 갱신

print(result)




