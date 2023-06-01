# 돌 게임

import sys
input = sys.stdin.readline

# 홀수엔 상근,, 짝수엔 창영..?
n = int(input())
print('SK' if n%2==1 else 'CY')