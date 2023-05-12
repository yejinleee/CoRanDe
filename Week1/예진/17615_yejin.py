import sys
input = sys.stdin.readline

n = int(input())
li = list(input().rstrip())

cntR = li.count('R')
cntB = li.count('B')
lastR = lastB =0
ansfront = 0 #출력할 답
ansback = 0

if li[0] == 'R':
  for i in range(0,n):
    if li[i]=='R': lastR+=1
    else: break
  ansfront = min(cntR-lastR, cntB)
else:
  for i in range(0,n):
    if li[i]=='B' : lastB+=1
    else: break
  ansfront = min(cntB-lastB, cntR)

lastR = lastB =0
if li[-1]=='R':
  for i in range(n-1,-1,-1):
    if li[i]=='R': lastR+=1
    else: break
  ansback = min(cntB, cntR-lastR)
else:
  for i in range(n-1,-1,-1):
    if li[i]=='B': lastB+=1
    else: break
  ansback = min(cntR, cntB-lastB)

print(min(ansfront,ansback))