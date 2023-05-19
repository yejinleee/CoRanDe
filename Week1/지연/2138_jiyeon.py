import sys

N = int(sys.stdin.readline())

now = list(sys.stdin.readline().strip())
target = list(sys.stdin.readline().strip())

now_1 = list(map(int, now))
now_2 = list(map(int, now))
target = list(map(int, target))
ans = False
count = 1000000
#1번 스위치를 누르지 않은 경우
cnt = 0
for i in range(1, N):
    if now_1[i-1] != target[i-1]:
        now_1[i-1] = 1 - now_1[i-1]
        now_1[i] = 1 - now_1[i]
        if i != N-1:
            now_1[i+1] = 1 - now_1[i+1]
        cnt += 1
if now_1 == target:
    ans = True
    count = cnt

#1번 스위치를 누르는 경우
for i in range(2):
    now_2[i] = 1 - now_2[i]
cnt = 1
for i in range(1, N):
    if now_2[i-1] != target[i-1]:
        now_2[i-1] = 1 - now_2[i-1]
        now_2[i] = 1 - now_2[i]
        if i != N-1:
            now_2[i+1] = 1 - now_2[i+1]
        cnt += 1
if now_2 == target:
    ans = True
    count = min(cnt, count)

if ans:
    print(count)
else:
    print(-1)