# 캡틴 이다솜

import sys
input = sys.stdin.readline

'''
층수 1 2 3  4   5  6  7
각각 1 3 6  10 15 21 28 (앞거에 +자기층수)
총합 1 4 10 20 35 56 84 120

입력 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
출력 1 2 3 1 2 3 4 2 3 1  2   3 4  2  3   4  5 3  4  1   2

입력값이 총합에 고대로 있으면 바로 1
만약 없으면 ex 5. 직전인4부터 [4]+[1] 인 2
6. 
[젤가까운 총합] + [입력값- 젤가까운총합] 
예를 들어 24면 젤가까운총합이 20.  [20] = 1
입력값에서20빼서 [4] = 1
'''

dp = [0,1]
total = [0,1]
n = int(input().rstrip())
i = 2
each = 1
## 총합 배열 만들기
## 현재 총합은 직전 총합 + 이번 층에 놓인 갯수
## 이번 층에 놓일 갯수 = 지난층에 놓인 갯수 + 층수
###### 이거 계산간단히 ..... ? i*(i+1) //2 머이런식으로도 하던데 뭘까? 
while True:
    each +=i
    if total[-1] + each <= n: ## 입력받은 수보다 작거나 같은 총합일떄까지만 구함
        total.append(total[-1] + each)
        i+=1
    else:
        break

totidx = 1
for i in range(2, n+1):
    dpmin = 300001
    if i in total: ## 가진대포수가 총합배열에 있는 수면 바로 1이니까 
        dp.append(1)
        totidx +=1
        continue
    ## 아닌경우,
    ## totidx = 총합배열수중 가진대포수랑 제일 가까우면서 작은 총합수임
    ## 그 수부터 총합배열 내의 조합으로 구하면 됨. 그 중 최소
    for j in range(totidx, 0, -1):
        dpmin = min(dpmin , dp[total[j]] + dp[i-total[j]])
    dp.append(dpmin)

print(dp[-1])