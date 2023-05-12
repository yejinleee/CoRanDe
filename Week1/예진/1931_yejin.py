import sys
input = sys.stdin.readline

n = int(input())
li =[]
for _ in range(n):
  li.append(tuple(map(int,input().split())))

li.sort()
li.sort(key=lambda x: x[1])

end=cnt=0
for time in li:

  if time[0]>=end:
    cnt+=1
    end=time[1]

print(cnt)