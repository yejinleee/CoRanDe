# 싸이버개강총회

import sys
input = sys.stdin.readline

s, e, q = input().split()
starttime = int(s.split(":")[0]) * 60 + int(s.split(":")[1])
endtime = int(e.split(":")[0]) * 60 + int(e.split(":")[1])
streamingEndtime = int(q.split(":")[0]) * 60 + int(q.split(":")[1])

li = []
checkli = []
while True:
    try:
        hm, name = input().split()
        chattime = int(hm.split(":")[0]) * 60 + int(hm.split(":")[1])
        if 0 <= chattime <= starttime:
            li.append(name)
        elif endtime <= chattime <= streamingEndtime:
            checkli.append(name)
    except:
        print(len(set(li) & set(checkli)))
        break
