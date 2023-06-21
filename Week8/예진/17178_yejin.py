# 줄서기 (골5)

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
li = []

for _ in range(n):
    l = input().split()
    for i in range(len(l)):
        alpha, num = l[i].split('-')
        if len(num)==1:
            l[i] = alpha+'-00'+num
        elif len(num)==2:
            l[i] = alpha+'-0'+num
    li+=l

'''
입장은 영어빠른순, 영어같다면 숫자 작은순.
젤 작은 사람이 대기줄 앞에 왔다가 들어가야 그다음이 가능이다.
'''
hall = deque(li)
queue = deque(sorted(li))
stack = []

while queue:
    q = queue.popleft()
    if stack and q == stack[-1]:
        stack.pop()
        continue
    if not hall:
        if stack and q == stack[-1]:
            stack.pop()
            continue
        else:
            break
    while hall and q != hall[0]:
        stack.append(hall.popleft())
    if hall and q == hall[0]:
        hall.popleft()

if not hall and not queue and not stack:
    print('GOOD')
else:
    print('BAD')


## 조건 분기에서 if stack, while hall 등 큐나 스택이 비어있지 않은지 확인해줘야 한다.
## 39번줄 while hall 해주지 않아서 indexError 발생했었음.
