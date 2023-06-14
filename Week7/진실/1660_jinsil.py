# 2. 캡틴 이다솜 (실1) PyPy3으로 통과

import sys
input = sys.stdin.readline

N = int(input())

dp1 = [0, 1]  #삼각형
dp2 = [0, 1]  #사면체
dp3 = [0, 1]  #결괏값

#삼각형과 사면체 dp 구함
i = 2
while True:
  dp1.append(dp1[i-1]+i)
  dp2.append(dp2[i-1]+dp1[i])
  if dp2[i] > N:
    break
  i += 1

#결괏값 구하기
for i in range(2, N+1):
  mv = 999
  j = 1
  while True:
    if dp2[j] > i:
      break
    mv = min(mv, dp3[i-dp2[j]])
    j += 1 
  dp3.append(mv+1)

print(dp3[N])