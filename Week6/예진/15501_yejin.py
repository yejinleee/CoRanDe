# 부당한 퍼즐

import sys
input = sys.stdin.readline

n = int(input())
puzzle = list(map(int, input().split()))
ans = list(map(int, input().split()))

'''
직접 뒤집기, 밀기 를 해보면서 확인해보는건 RecursionError: maximum recursion depth exceeded while calling a Python object
백트래킹으로 해도 너무 많은 호출

원리를 생각해보자
뒤집기를 하거나 밀기를 해도 바뀌지 않는건?
내 앞뒤가 무엇인지는 바꾸지 않는다.
만약 양끝이라면 맨뒤를 %로 확인해야할것이다.

내 앞은 (i-1)%n
내 뒤는 (i+1)%n

딕셔너리를 써야 할듯

예제1대로 만들어보면
{1: [5,2]}, {2: [1,3] } 이렇게 앞뒤 수가 무엇인지
{1: [5, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 1]}
'''
dic = {}
for i in range(n):
    dic[puzzle[i]] = [puzzle[(i-1)%n], puzzle[(i+1)%n]]

good = 1
for i in range(n):
    if ans[(i-1)%n] not in dic[ans[i]] or ans[(i+1)%n] not in dic[ans[i]]:
        good = 0
        break
print('good puzzle' if good == 1 else 'bad puzzle')