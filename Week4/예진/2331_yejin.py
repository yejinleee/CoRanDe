import sys
input = sys.stdin.readline

def makeDn(x,p):
    xli = list(map(int, str(x)))
    return sum(list(map(lambda x: x**p, xli)))

a, p = map(int, input().split())
d = [a]
i=1
while True:
    new = makeDn(d[i-1], p)
    if new in d:
        print(len(d[:d.index(new)]))
        break
    d.append(new)
    i+=1

''' 풀이
makeDn(x,p)함수 :
매개변수 x는 D[n-1]을 받아온다.
이 숫자를 각 자릿수별로 리스트를 만들기 위해 list(map(int, str(x)))
호긍ㄴ [int(a) for a in str(x)] 도 가능
'''