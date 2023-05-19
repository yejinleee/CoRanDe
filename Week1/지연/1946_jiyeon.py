import sys

T = int(sys.stdin.readline())

for _ in range(T):
    score = []
    N = int(sys.stdin.readline())
    for __ in range(N):
        score.extend([list(map(int, sys.stdin.readline().split()))])
    
    score.sort()
    min = score[0][1]
    cnt = 0
    for i in range(1, N):
        if score[i][1] < min:
            min = score[i][1]
        if score[i][1] > min:
            cnt += 1
        
    print(N-cnt)