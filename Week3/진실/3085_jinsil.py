# 15. 사탕 게임 (실3) 

import sys
input = sys.stdin.readline

N = int(input())
C = [list(input().rstrip()) for _ in range(N)]

def max_color(array): # 연속된 색의 최댓값 세주는 함수
  result = 0
  for i in range(len(array[0])):  
    # 가로 확인
    a = array[i] #가로 배열
    init = a[0]
    max_a = 0
    cnt = 1
    for j in range(1, len(array[0])):
      if a[j] == init :
        cnt += 1
      else :
        init = a[j]
        cnt = 1
      if cnt > max_a :
        max_a = cnt

    # 세로 확인
    b = [c[i] for c in array] #세로 배열
    init = b[0]
    max_b = 0
    cnt = 1
    for j in range(1, len(array[0])):
      if b[j] == init :
        cnt += 1
      else :
        init = b[j]
        cnt = 1
      if cnt > max_b :
        max_b = cnt
    
    #가로, 세로 중 더 큰 값을 result에 갱신
    if max(max_a, max_b) > result:
      result = max(max_a, max_b)
  return result

r = [] #max_color의 반환값을 모두 넣는 배열
for i in range (N):
  for j in range (N):
    if i != 0 :
      C[i][j], C[i-1][j] = C[i-1][j], C[i][j] #위치 바꿈
      r.append(max_color(C)) #함수 통해 확인 후
      C[i][j], C[i-1][j] = C[i-1][j], C[i][j] #위치 다시 바꿈
    if j != 0 :
      C[i][j], C[i][j-1] = C[i][j-1], C[i][j]
      r.append(max_color(C))
      C[i][j], C[i][j-1] = C[i][j-1], C[i][j]
    if i != N-1 :
      C[i][j], C[i+1][j] = C[i+1][j], C[i][j]
      r.append(max_color(C))
      C[i][j], C[i+1][j] = C[i+1][j], C[i][j]
    if j != N-1 :
      C[i][j], C[i][j+1] = C[i][j+1], C[i][j]
      r.append(max_color(C))
      C[i][j], C[i][j+1] = C[i][j+1], C[i][j]

#최댓값 갱신 하는 것이 아닌 모든 값을 배열에 넣은 후 거기서 최댓값 출력
print(max(r)) 