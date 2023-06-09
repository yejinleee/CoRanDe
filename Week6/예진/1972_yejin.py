# 놀라운 문자열


from itertools import permutations
import sys
input = sys.stdin.readline

surstr = input().rstrip()
while surstr != '*':
    alphabetlist = list(surstr)
    cb = permutations(alphabetlist, 2)
    strdicor = dict()
    for c in cb :
        strdicor[c[0]+c[1]] = 0
    surprising = 1
    for i in range(1,len(surstr)):
        strdic = strdicor.copy()
        for j in range(0, len(surstr) - i):
            strdic[str(surstr[j] + surstr[j+i])] +=1
        strdic2 = sorted(strdic.items(), key = lambda x : x[1])
        if strdic2[-1][1] > 1 :
            surprising = 0
            break
    print(surstr, end='')
    print(' is surprising.' if surprising else ' is NOT surprising.')
    
    surstr = input().rstrip()


'''
일단 가능한 순열 다 계산. 정렬때문에 순열해야할듯
asdf면
as,ad,af,sd,sf,df
이걸 딕셔너리로 만들고
D-쌍 구하면서 값 증가
중복으로 등장했으면 {'as': 2} 이렇게 됐을테니 정렬해서 큰값이 1보다 크면 NOT surprising

'''