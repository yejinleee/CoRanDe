import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[int(j) for j in input().rstrip()] for i in range(N)]
B = [[int(j) for j in input().rstrip()] for i in range(N)]

cnt= 0

def reverse(si,sj):
  for i in range(si,si+3):
    for j in range(sj, sj+3):
      A[i][j] = 1 - A[i][j]
def check():
  for i in range(N):
    for j in range(M):
      if A[i][j]!=B[i][j]:
        return False
  return True

# 미리 N<3 or M<3 검사 하면 오답
# 왜 ?
for i in range(N-2):
  for j in range(M-2):
    if (A[i][j] != B[i][j]):
      reverse(i,j)
      cnt+=1
if check():
  print(cnt)
else:
  print(-1)
      