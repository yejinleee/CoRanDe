import sys

N = int(sys.stdin.readline())
An = list(map(int, sys.stdin.readline().split()))
symbol = list(map(int, sys.stdin.readline().split()))

minNum = int(1e9)
maxNum = int(-1e9)

answer = An[0]

def dfs(idx):
    global answer
    global minNum, maxNum

    if idx == N:
        if answer > maxNum:
            maxNum = answer
        if answer < minNum:
            minNum = answer
        return

    for i in range(4):
        tmp = answer
        if symbol[i] > 0:
            if i == 0:
                answer += An[idx]
            elif i == 1:
                answer -= An[idx]
            elif i == 2:
                answer *= An[idx]
            else:
                if answer >= 0:
                    answer //= An[idx]
                else:
                    answer = (-answer // An[idx]) * -1

            symbol[i] -= 1
            dfs(idx+1)
            answer = tmp
            symbol[i] += 1

dfs(1)
print(maxNum)
print(minNum)