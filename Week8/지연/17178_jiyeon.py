import sys
import itertools
from collections import deque
import re

N = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().strip().split()) for _ in range(N)]

order = list(itertools.chain(*arr))
p = re.compile(r'\d+')
order = sorted(order, key=lambda s: (s[0], int(p.search(s).group())))
order = deque(order)

wating = deque()
for i in range(N):
    for ticket in arr[i]:
        while len(wating) > 0:
            if wating[-1] == order[0]:
                wating.pop()
                order.popleft()
            else:
                break
        if ticket == order[0]:
            order.popleft()
            continue
        wating.append(ticket)

for i in range(len(wating)):
    if order.popleft() != wating.pop():
        print("BAD")
        exit()

print("GOOD")