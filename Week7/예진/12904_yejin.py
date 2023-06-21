import sys
input = sys.stdin.readline

S= input().rstrip()
T = input().rstrip()

Tlist = list(T)
n = len(Tlist)
result=0
for i in range(n-1,-1,-1):
  if Tlist[i]=='B':
    Tlist.pop()
    Tlist.reverse()
  else: #'A'
    Tlist.pop()
  if Tlist==list(S):
    result=1
    break

print(result)
