import sys

N = int(sys.stdin.readline())

meeting = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append([end, start])

meeting.sort(key=lambda x: (x[0], x[1]))

end = meeting[0][0]
cnt = 1

for i in range(1, N):
    if meeting[i][1] >= end:
        cnt += 1
        end = meeting[i][0]

print(cnt)