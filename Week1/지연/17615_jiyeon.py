import sys

N = int(sys.stdin.readline())

ball = list(sys.stdin.readline().strip())

rcnt = ball.count('R')
bcnt = ball.count('B')

mball = min(rcnt, bcnt)

#왼쪽에 옮기는 경우
cnt = 0
for i in range(N):
    if ball[i] != ball[0]:
        break
    cnt += 1
if ball[0] == 'R':
    mball = min(mball, rcnt-cnt)
else:
    mball = min(mball, bcnt-cnt)

#오른쪽에 옮기는 경우
cnt = 0
for i in range(N-1, -1, -1):
    if ball[i] != ball[N-1]:
        break
    cnt += 1
if ball[N-1] == 'R':
    mball = min(mball, rcnt-cnt)
else:
    mball = min(mball, bcnt-cnt)

print(mball)