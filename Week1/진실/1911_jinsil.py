# 25. 흙길 보수하기(실1) 맞음

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pool = []
for i in range(N) :
  pool.append(list(map(int, input().split())))

pool.sort()

result = 0
start = pool[0][0]
end = ((pool[0][1]-start+L-1)//L)*L + start #start값에서 L의 배수를 더한 값

for i in range (N) :
  if end < pool[i][0] : #end값이 현재 웅덩이 시작값보다 작다면
    result += (end-start+L-1)//L #널빤지 개수 더해줌
    start = pool[i][0] #start값을 현재 웅덩이 시작값으로 갱신
    end = ((pool[i][1]-start+L-1)//L)*L + start #end값을 start값에서 L의 배수 더한 값으로 갱신
  else : #end값이 현재 웅덩이 시작값보다 크다면
    end = ((pool[i][1]-start+L-1)//L)*L + start #end값만 갱신

result += (end-start+L-1)//L #마지막 널빤지 개수 더해줌
print(result)