# 3. 요세푸스 문제 (실4)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i+1 for i in range(N)] 

result = '<'
idx = 0
end = N
for i in range(N):
  idx = (idx+K-1)%end
  result += str(arr[idx])
  end -= 1
  arr.pop(idx)

  if i == N-1:
    break
  result += ', '

result += '>'
print(result)
