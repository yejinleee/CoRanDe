import sys
input = sys.stdin.readline

n = int(input())
candy = []
for _ in range(n):
    candy.append(list(input().rstrip()))
# print(candy)

# ##### 행렬 전환
# candyT = list(map(list, zip(*candy)))

# def checkNS(li, i,j,n):
#     if i!=0:
#         if li[i-1][j] == li[i][j-1]:
#             return 1
#     if i!=n-1:
#         if li[i+1][j] == li[i][j-1]:
#             return 1
#     return 0

# def checkEW(li,i,j,n):
#     if j!=n-1:
#         if li[i][j+1]==li[i][j-1]:
#             return 1
#             nncnnnnnn

# maxCnt =1
# for i in range(n):
#     cnt=1
#     flag=0 #교환 사용했으면1, 아니면 0
#     for j in range(1,n):
#         if candy[i][j] == candy[i][j-1]:
#             cnt+=1
#             if j==n-1:
#                 if cnt>maxCnt:
#                     maxCnt=cnt
#         else:
#             if flag: #이미 앞에서 교환사용했으면 카운트값만 비교하고 초기화해야함
#                 if cnt>maxCnt:
#                     maxCnt=cnt
#                 cnt=0
#             else: #앞에서 교환없던 경우면 교환되는지 확인
#                 if checkNS(candy, i,j,n): #위아래랑 교환하면 연결될때
#                     flag=1
#                     cnt+=1
#                 else:
#                     if cnt>maxCnt:
#                         maxCnt=cnt
#                     cnt=0

# for i in range(n):
#     cnt=1
#     flag=0 #교환 사용했으면1, 아니면 0
#     for j in range(1,n):
#         if candyT[i][j] == candyT[i][j-1]:
#             cnt+=1
#             if j==n-1:
#                 if cnt>maxCnt:
#                     maxCnt=cnt
#         else:
#             if flag: #이미 앞에서 교환사용했으면 카운트값만 비교하고 초기화해야함
#                 if cnt>maxCnt:
#                     maxCnt=cnt
#                 cnt=0
#             else: #앞에서 교환없던 경우면 교환되는지 확인
#                 if checkNS(candyT, i,j,n): #위아래랑 교환하면 연결될때
#                     flag=1
#                     cnt+=1
#                 else:
#                     if cnt>maxCnt:
#                         maxCnt=cnt
#                     cnt=0

# print(maxCnt)
######### 행을 훑으면서 교환해서 연결되는지 확인하려 했으나 같은 행에서 좌우 교환할때 경우가 까다롭다 ㅇㅅㅇ;;


# 그냥 다 해보는 방법..

def cntMax(arr):
    global n
    maxcnt=1

    for i in range(n):
        cnt=1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt=1
            if cnt > maxcnt:
                maxcnt = cnt

        cnt=1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt=1
            if cnt > maxcnt:
                maxcnt = cnt
    return maxcnt

maxCnt=0
for i in range(n):
    for j in range(n):
        if j+1 < n:
        	# 좌우 교환
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            # 교환한 candy배열에 대하여 이어지는 maxcnt찾기
            temp= cntMax(candy)
            if temp > maxCnt:
                maxCnt = temp
            # 원래대로
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        # 행 바꾸기
        if i+1 < n:
        	# 상하교환
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            temp=cntMax(candy)
            if temp > maxCnt:
                maxCnt = temp
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            
print(maxCnt)