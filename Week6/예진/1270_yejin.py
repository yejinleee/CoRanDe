# 전쟁 - 땅따먹기

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    army = list(map(int,input().split()))
    num = army[0]
    armydic = {}
    for i in range(1,num +1):
        if army[i] in armydic:
            armydic[army[i]] +=1
        else:
            armydic[army[i]] = 1
    armydic = sorted(armydic.items(), key=lambda x: x[1])
    print(armydic[-1][0] if armydic[-1][1] > num/2 else 'SYJKGW')
