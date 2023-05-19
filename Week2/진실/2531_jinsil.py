# 34.회전 초밥 (실1)

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
S = [int(input()) for _ in range(N)]

result = 0
arr = S[0:k]
K = [0]*(d+1) #초밥 종류 배열

for i in range(k):
  K[arr[i]] += 1
K[c] += 1

for i in range(N):
  if (d+1)-K.count(0) > result: #배열K 에서 0이 아닌 것의 개수
    result = (d+1)-K.count(0)

  K[arr.pop(0)] -= 1 #첫 요소 삭제
  arr.append(S[(i+k)%N]) #다음 요소 추가
  K[S[(i+k)%N]] += 1

print(result)
