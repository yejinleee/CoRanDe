# 설탕배달

# dp로 44ms
import sys
input = sys.stdin.readline

n = int(input())
dpt = [1667]*(n+1) ## 초기화 주의!
dpt[0] = 0
for i in [5,3]:
    for j in range(3,n+1):
        if dpt[j - i] != 1667:
            dpt[j] = min(dpt[j], dpt[j-i] +1)
print(dpt[-1] if dpt[-1] != 1667 else -1)

## 4999입력시 필요한 최소가 1001번임.. INF랑 구분필요 .. !


# 구현으로 풀면 68 ms 

# import sys
# n = int(sys.stdin.readline())
# cnt =0
# while n>=0:
#   if n%5 ==0: #5의 배수
#     cnt+= n//5
#     print(cnt)
#     break
#   n-=3
#   cnt+=1
# if n<0:
#   print(-1)

# 1등풀이 32ms ^^
# x = int(input())
# a = 0
# while x >= 0:
#     if x % 5 == 0:
#         a += (x//5)
#         print(a)
#         break
#     x = x - 3
#     a = a + 1
# else:
#     print(-1)

## while ~ else 
## for ~ else
## 반복문 돌다가 반복문 조건에 위반되었을 때 실행됨