import sys
input = sys.stdin.readline

t = int(input())

# 풀 1 -> 시간 초과
# 남은 날 중 지금이 최대가 아니면 팔지않고 산다.
# 최대인 날 다 판다.
'''
for _ in range(t):
  n = int(input())
  li = list(map(int,input().split()))
  profit =0
  cnt =0
  holding=0
  maxStock = max(li)
  for j in range(n):
    if li[j] == maxStock:
      profit+= li[j]*cnt - holding
      cnt=0
      holding=0
    else:
      holding+= li[j]
      cnt+= 1
    if j!=n-1:
      maxStock= max(li[j+1:])
  print(profit)
'''

## 풀2
## 계산을 줄여보자
'''
for _ in range(t):
  n = int(input())
  li = list(map(int,input().rstrip().split()))
  maxli = sorted(li, reverse=True)
  profit= 0
  for i in range(n):
    if li[i] == maxli[0]:
      maxli.pop(0)
    else:
      profit+= maxli[0]-li[i]
      ## 계산한 값 maxli에서 지워줘야한다!! 그값이 어느날엔 최대로 여겨질 수 있으니까ㅈ!!!
      maxli.remove(li[i])
  print(profit)
## -> 시간 초과 ..^^
'''

### 풀3
### 다른 배열과 비교, max() 모두 없이
for _ in range(t):
  n = int(input())
  li = list(map(int,input().rstrip().split()))
  profit= 0
  max=li[n-1]
  for i in range(n-1,-1,-1):
    if li[i]<max:
      profit+= max-li[i]
    else:
      max=li[i]
  print(profit)