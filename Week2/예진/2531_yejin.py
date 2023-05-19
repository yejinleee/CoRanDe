import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
c = str(c)
sushi = []
for _ in range(n):
    sushi.append(input().rstrip())

for i in range(k):
    sushi.append(sushi[i])

check =[]
maxlen = 0
for i in range(n):
    check = sushi[i:i+k] # 이중 for문이 시간초과를 발생시킨다.
    check.append(c)
    maxlen = max(maxlen, len(set(check)))

print(maxlen)


'''
반례
8 30 4 30
7
7
3
7
7
8
7
7

>> 4
'''