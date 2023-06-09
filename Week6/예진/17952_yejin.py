# 과제는 끝나지 않아!

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
last = deque([])
point = 0
for i in range(n):
    ipt = input().rstrip()
    if ipt=='0':
        if last:
            prevgrade,prevtime = last.popleft()
            if prevtime >1 :
                last.appendleft((grade, prevtime-1))
            else:
                point+= prevgrade
    else:
        one, grade, time = map(int, ipt.split())
        if time >1 :
            last.appendleft((grade, time-1))
        else:
            point += grade
print(point)


### 큐.appendleft()
### insert(0,값) 아니고 appendleft()를 사용해서 Double-ended Queue로 사용 가능하다!
### 시간복잡도 O(1) 임.