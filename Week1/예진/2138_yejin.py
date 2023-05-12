import sys
input = sys.stdin.readline

n = int(input())
now = [int(i) for i in input().rstrip()]
goal = [int(i) for i in input().rstrip()]
now2=now.copy()

def change(i):
  if i==0: return 1
  else: return 0

#일단 맨앞거를 누르는 경우
cnt1=1
now[0]=change(now[0])
now[1]=change(now[1])
#맨앞거 안누르는 경우
cnt2=0

for i in range(1,n):
  if now[i-1]!=goal[i-1]:
    cnt1+=1
    now[i]=change(now[i])
    now[i-1]=change(now[i-1])
    if i!=n-1:
      now[i+1]=change(now[i+1])
  if now2[i-1]!=goal[i-1]:
    cnt2+=1
    now2[i]=change(now2[i])
    now2[i-1]=change(now2[i-1])
    if i!=n-1:
      now2[i+1]=change(now2[i+1])
      
if now!=goal:
  cnt1=100001
if now2!=goal:
  cnt2=100001
# print(cnt1,cnt2)
if cnt1==100001 and cnt2==100001:
  print(-1)
else:
  print(min(cnt1,cnt2))