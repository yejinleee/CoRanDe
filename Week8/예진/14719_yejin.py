# 빗물 (골5)

import sys
input = sys.stdin.readline

h, w = map(int,input().split())
li = list(map(int,input().split()))

tot =0
for i in range(1,w-1):
    low = min(max(li[:i]), max(li[i+1:]))
    if low > li[i]:
        tot += low - li[i]
print(tot)


'''
풀이 원리 :
본인기준 양 옆 각각 젤 높은 수를 찾고
그 둘 중 작은 값(=low)과 자신의 차 만큼 빗물이 고일 수 있다.

검사는 [1] 부터 [w-2]까지 검사한다.
왜? 어짜피 [0]이랑 [w-1]은 양끝이라 위로 쌓일 수 없으니까
'''