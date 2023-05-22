import sys
from itertools import permutations
input = sys.stdin.readline

# 서로 다!른! 세자리
num = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3)) 
lennum=504

n = int(input())
result=0
for i in range(n):
    mh, s, b = map(int, input().split())
    mh= list(str(mh))
    ln =0
    while ln<len(num):
        cntS=cntB= 0
        for j in range(3):
            if int(mh[j]) == num[ln][j]:
                cntS+=1
                continue
            elif int(mh[j]) in num[ln]:
                cntB+=1
                continue
        if cntS!=int(s) or cntB !=int(b):
            num.remove(num[ln])
        else :
            ln+=1

print(len(num))