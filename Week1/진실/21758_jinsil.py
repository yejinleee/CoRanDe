# 33. 꿀 따기(골5) 맞음

import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

# 벌-꿀통-벌
result1 = 0
part1 = 0
part2 = sum(X)-X[0]-X[N-1]
for i in range (1, N-1) :
  part2 -= part1
  part1 += X[i]
  if part1+part2 > result1 :
    result1 = part1+part2

# 벌-벌-꿀통
result2 = 0
part1 = sum(X)-X[0]
part2 = sum(X)-X[0]
for i in range (1, N) :
  part2 -= X[i]
  s = (part1-X[i])+part2
  if s > result2 :
    result2 = s

# 꿀통-벌-벌
X.reverse()
result3 = 0
part1 = sum(X)-X[0]
part2 = sum(X)-X[0]
for i in range (1, N) :
  part2 -= X[i]
  s = (part1-X[i])+part2
  if s > result3 :
    result3 = s

# 세개 다 구해서 그 중 제일 큰 값 출력
result = max(result1, result2, result3)

print(result)


