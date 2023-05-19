# 40. 전구와 스위치(골5) 질문검색 참고함

N = int(input())
A = list(map(int, str(input())))
B = list(map(int, str(input())))

a1 = A[:]
a2 = A[:]
#첫 번째 스위치 누름
a1[0] = int(not a1[0])
a1[1] = int(not a1[1])
result1 = 1
for i in range (1, N):
  if a1[i-1] != B[i-1]:
    a1[i-1] = int(not a1[i-1])
    a1[i] = int(not a1[i])
    if i < N-1:
      a1[i+1] = int(not a1[i+1])
    result1 += 1

#첫 번째 스위치 안 누름
result2 = 0
for i in range (1, N):
  if a2[i-1] != B[i-1]:
    a2[i-1] = int(not a2[i-1])
    a2[i] = int(not a2[i])
    if i < N-1:
      a2[i+1] = int(not a2[i+1])
    result2 += 1

if a1 == B and a2 == B:
  print(min(result1, result2))
elif a1 == B :
  print(result1)
elif a2 == B :
  print(result2)
else :
  print(-1)
