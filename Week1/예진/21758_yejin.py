import sys
input = sys.stdin.readline

n = int(input())
honeylist = list(map(int, input().split()))

def findMaxHoney(n,honeylist):
  if len(honeylist)==3:
    print(max(honeylist)*2)
    return
  maxhoney=0
  
  # 벌통 . . . 벌 . .벌
  sumToLeft = sum(honeylist)-honeylist[-1]
  fromi=sumToLeft
  for i in range(len(honeylist)-2,-1,-1):
    fromi-= honeylist[i]
    if (sumToLeft-honeylist[i]) + fromi > maxhoney:
      maxhoney = (sumToLeft-honeylist[i]) + fromi
    
  # 벌 . .벌 . . .벌통
  sumToRight = sum(honeylist)-honeylist[0]
  fromi=sumToRight
  for i in range(1,len(honeylist)):
    fromi-= honeylist[i]
    if (sumToRight-honeylist[i]) + fromi > maxhoney:
      maxhoney = (sumToRight-honeylist[i]) + fromi
    
  # 벌 . . . 벌통 . . .ㅂ 벌
  sumMid = sum(honeylist)-honeylist[0]-honeylist[-1]
  for i in range(1,len(honeylist)-1):
    if sumMid+honeylist[i] > maxhoney:
      maxhoney = sumMid+honeylist[i]
      
  print(maxhoney)
  return

findMaxHoney(n, honeylist)