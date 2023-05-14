import sys

N = int(sys.stdin.readline())

def solve(paper):
    if len(paper) <= 1:
        return True

    flag = True
    mid = len(paper) //2
    for i in range(mid):
        if paper[i] == paper[-(i+1)]:
            flag = False
            break

    if flag:
        return solve(paper[:mid]) and solve(paper[mid+1:])
    else:
        return False

for _ in range(N):
    str = sys.stdin.readline().strip()
    paper = list(map(int, str))
    if solve(paper):
        print('YES')
    else:
        print('NO')