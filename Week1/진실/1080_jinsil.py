# 32. 행렬(실1) 맞음

N, M = map(int, input().split())
A = []
B = []
for i in range(N):
  A.append(list(map(int, input())))
for i in range(N):
  B.append(list(map(int, input())))


if N < 3 or M < 3 :
  if A == B :
    print(0)
  else :
    print(-1)

else : 
  result = 0
  for i in range(N-2):
    for j in range (M-2):
      if A[i][j] != B[i][j]:
        A[i][j] = int(not A[i][j])
        A[i][j+1] = int(not A[i][j+1])
        A[i][j+2] = int(not A[i][j+2])
        A[i+1][j] = int(not A[i+1][j])
        A[i+1][j+1] = int(not A[i+1][j+1])
        A[i+1][j+2] = int(not A[i+1][j+2])
        A[i+2][j] = int(not A[i+2][j])
        A[i+2][j+1] = int(not A[i+2][j+1])
        A[i+2][j+2] = int(not A[i+2][j+2])
        result += 1
  if A == B :
    print(result)
  else :
    print(-1)
