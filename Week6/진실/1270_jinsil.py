# 6. 전쟁 - 땅따먹기(실3)
# 시간 줄여보기

import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
  T = list(map(int, input().split()))
  dic = {}
  for j in range(1, T[0]+1):
    if T[j] not in dic:
      dic[T[j]] = 1
    else:
      dic[T[j]] += 1
  dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
  if dic[0][1] > T[0]/2:
    print(dic[0][0])
  else:
    print("SYJKGW")