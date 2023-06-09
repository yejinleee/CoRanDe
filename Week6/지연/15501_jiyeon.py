import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = list(map(int, sys.stdin.readline().split()))

arrnum = dict()

for i in range(N):
    if i == 0:
        start = N-1
        end = i+1
    elif i == N-1:
        start = i-1
        end = 0
    else:
        start = i-1
        end = i+1
    arrnum[arr[i]] = [start, end]

flag = 1
if len(arr) == 1:
    print("good puzzle")
else:
    for i in range(N):
        start, end = arrnum[ans[i]]
        if i == 0:
            s = N-1
            e = i+1
        elif i == N-1:
            s = i-1
            e = 0
        else:
            s = i-1
            e = i+1
        if ((arr[start] == ans[s]) and (arr[end] == ans[e])) or ((arr[start] == ans[e]) and (arr[end] == ans[s])):
            continue
        else:
            flag = 0
            break
    if flag:
        print("good puzzle")
    else:
        print("bad puzzle")