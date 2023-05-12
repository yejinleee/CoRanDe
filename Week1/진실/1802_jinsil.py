# 23. 종이접기(실2) 맞음

import sys

T = int(sys.stdin.readline())

for i in range (T) :
  P = input()
  P = list(map(int, str(P)))

  # 2^N-1 길이만 입력이므로 N을 구할 수 있다
  N = 0
  length = len(P)+1
  while length > 1 :
    length /= 2
    N += 1
  
  # 플래그 1이고, 반으로 계속 접으면서 마주보는 값의 합이 1이 아니면 플래그를 0으로 해줌
  f = 1
  for j in range (N, 0, -1) :
    n = 2**j-2
    for k in range(n//2) :
      if P[k]+P[n-k] != 1 :
        f = 0

  # 플래그가 여전히 1이라면 yes, 0으로 바뀌었다면 no
  if f == 1 :
    print('YES')
  else :
    print('NO')