import sys

exp = list(sys.stdin.readline().rstrip())

nlist = []
symbol = []

num = 0
for i in range(len(exp)):
    if (exp[i] == '+') or (exp[i] == '-'):
        symbol.append(str(exp[i]))
        nlist.append(num)
        num = 0
    else:
        num = num*10 + int(exp[i])


nlist.append(num)
sum = 0
idx = 0
for i in range(len(symbol)): 
    if symbol[i] == '+':
        nlist[idx] = nlist[idx] + nlist[idx+1]
        del nlist[idx+1]
    else:
        idx += 1

if len(nlist) > 1:
    for i in range(1, len(nlist)):
        sum += nlist[i]
    print(nlist[0]-sum)
else:
    print(nlist[0])