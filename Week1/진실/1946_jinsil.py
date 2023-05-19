# 26. 신입사원(실1) 맞음

import sys
input = sys.stdin.readline

T = int(input())
R = ""

# 입력 받으면서 바로 해야함 안 그러면 3중 for문됨
for i in range (T) :
  p = []
  N = int(input())
  for j in range (N) :
    p.append(list(map(int, input().split())))
  p.sort() # 서류 기준으로 정렬

  result = 1 # 서류 1등은 무조건 선발됨
  m = p[0][1] # 최솟값은 서류 1등의 면접 점수
  for j in range(1, N) :
    if m > p[j][1] : # 현재 사원이 앞 사람들 서류 1등보다 등수가 높으면 선발
      m = p[j][1] # 최솟값 갱신
      result += 1
      
  R += (str(result) + '\n')

print(R)

 
