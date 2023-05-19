import sys
input = sys.stdin.readline

n= int(input())
nlist = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
mintotal = 1000000000
maxtotal = -1000000000


def check(i, result, plus, minus, mul, div):
    global mintotal, maxtotal

    if i ==n:
        mintotal = min(mintotal, result)
        maxtotal = max(maxtotal, result)
        return
    if plus > 0:
        check(i+1, result+nlist[i], plus-1, minus, mul, div)
    if minus > 0 :
        check(i+1, result-nlist[i], plus, minus-1, mul, div)
    if mul > 0:
        check(i+1, result*nlist[i], plus, minus, mul-1, div)
    if div > 0:
        check(i+1, int(result / nlist[i]), plus, minus, mul, div-1)



check(1, nlist[0], plus, minus, mul, div)
print(maxtotal)
print(mintotal)


# 15658 이랑 뭐가 다를가요?