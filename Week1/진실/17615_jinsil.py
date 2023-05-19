# 39. 볼 모으기(실1)

import sys
input = sys.stdin.readline

N = int(input())
ball = input().rstrip()

#빨간 공 뒤로
result1 = 0
cnt = 0
f = 0
for i in range (N):
  if ball[i] == 'R':
    if f == 1 :
      result1 += cnt
      cnt = 0
      f = 0
    cnt += 1
  else :
    f = 1
if f == 1 :
  result1 += cnt

#빨간 공 앞으로
result2 = 0
cnt = 0
f = 0
for i in range (N-1, -1, -1):
  if ball[i] == 'R':
    if f == 1 :
      result2 += cnt
      cnt = 0
      f = 0
    cnt += 1
  else :
    f = 1
if f == 1 :
  result2 += cnt

#파란 공 뒤로
result3 = 0
cnt = 0
f = 0
for i in range (N):
  if ball[i] == 'B':
    if f == 1 :
      result3 += cnt
      cnt = 0
      f = 0
    cnt += 1
  else :
    f = 1
if f == 1 :
  result3 += cnt

#파란 공 앞으로
result4 = 0
cnt = 0
f = 0
for i in range (N-1, -1, -1):
  if ball[i] == 'B':
    if f == 1 :
      result4 += cnt
      cnt = 0
      f = 0
    cnt += 1
  else :
    f = 1
if f == 1 :
  result4 += cnt

  
print(min(result1, result2, result3, result4))