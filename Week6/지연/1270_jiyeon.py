import sys

n = int(sys.stdin.readline())

for _ in range(n):
    army = dict()
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(arr)):
        if arr[i] not in army: #딕셔너리에 군대 저장함
            army[arr[i]] = 1
        else:
            army[arr[i]] += 1
    idx = max(army, key=army.get) #최댓값의 인덱스 찾아서
    if army[idx] > arr[0]//2: #그 값이 절반이상이면 출력
        print(idx)
    else: #아니면 전쟁중 표시
        print("SYJKGW")