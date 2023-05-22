# 요세푸스 문제

## 6156ms ... .^^
# import sys
# input = sys.stdin.readline
# from collections import deque

# n, k =map(int,input().split())
# out = []
# li = [i for i in range(1,n+1)]
# queue = deque(li)

# cnt = 0
# while queue:
#     q = queue.popleft()
#     cnt +=1
#     if cnt != k:
#         queue.append(q)
#     else:
#         out.append(q)
#         cnt =0

# print('<',end='')
# print(', '.join(map(str,out)),end='')
# print('>',end='')
# print('')


### 참고
### 52ms 

import sys
input = sys.stdin.readline

'''
1 2 3 4 5 6 7
3 -> 6 -> 2 순이니까 3 이 사라지고 [2]=4임. [2]부터 세번째는 [4]인 6.
사라지고나서 다음 사라질애와 인덱스 차이가 2인셈 즉, k-1 !
'''

n, k =map(int,input().split())
out = []
li = [i for i in range(1,n+1)]

cnt = 0
while len(li) >0:
    cnt += k-1
    if cnt >= len(li):
        cnt %= len(li)
    out.append(li.pop(cnt))
print('<',end='')
print(', '.join(map(str,out)),end='')
print('>',end='')
print('')
