import sys

N = int(sys.stdin.readline())

place = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0] * (N+1)

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + place[i-1]

ans = [0,0,0]

if N == 3:
    ans = [max(place)*2]
else:
    #벌-벌-꿀인 경우
    for i in range(1, N-1):
        b1 = prefix_sum[N] - prefix_sum[1] - place[i]
        b2 = prefix_sum[N] - prefix_sum[i+1]
        ans[0] = max(ans[0] , b1+b2)

    #꿀-벌-벌인 경우
    for i in range(1, N-1):
        b1 = prefix_sum[N-1]-place[i]
        b2 = prefix_sum[i]
        ans[1] = max(ans[1] , b1+b2)

    #벌-꿀-벌인 경우
    for i in range(1, N-1):
        b1 = prefix_sum[i+1] - prefix_sum[1]
        b2 = prefix_sum[N-1] - prefix_sum[i]
        ans[2] = max(ans[2] , b1+b2)

print(max(ans))