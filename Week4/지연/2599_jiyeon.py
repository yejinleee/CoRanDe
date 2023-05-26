import sys

# a = A남자, B여자
# b = A남자, C여자
# c = B남자, A여자
# d = B남자, C여자
# e = C남자, A여자
# f = C남자, B여자

# https://settembre.tistory.com/73 <- 이거 참고해서 풀렸는데 틀렸쥬
N = int(sys.stdin.readline())

male = []
female = []

flag = 0

for _ in range(3):
    m, f = map(int,sys.stdin.readline().split())
    male.append(m)
    female.append(f)

for i in range(male[0]+1):
    a = i
    d = male[0] - a
    e = female[2] - d
    b = male[1] - e
    c = female[0] - b
    f = male[2] - c

    if a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0 and f >= 0:
        flag = 1
        break

if flag:
    print(1)
    print(a, d)
    print(b, e)
    print(c, f)
else:
    print(0)
