import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(3):
    boy, girl = map(int, input().split())
    li.append(boy)
    li.append(girl)

canmake = 0
for i in range(0, li[0]+1):
    AbBg = i
    AbCg = li[0] - i
    BbCg = li[5] - AbCg
    BbAg = li[2] - BbCg
    CbBg = li[3] - i
    CbAg = li[4] - CbBg
    if AbBg>=0 and AbCg>=0 and BbCg >=0 and BbAg >=0 and CbBg >=0 and CbAg >=0:
        print(1)
        print(AbBg, AbCg)
        print(BbAg, BbCg)
        print(CbAg, CbBg)
        canmake = 1
        break
if canmake == 0:
    print(0)


# 참고
# https://settembre.tistory.com/73