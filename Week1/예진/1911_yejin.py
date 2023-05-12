import sys
input = sys.stdin.readline

n, l = map(int, input().split())
li = []

for _ in range(n):
  li.append(tuple(map(int, input().split())))
li.sort()

e = cnt = 0
for m in li:
  if m[0] >= e:
    s = m[0]
  else:
    if m[1] >= e:
      s = e
    else:
      continue  #아래코드를 실행하지 않는다
  if (m[1] - s) % l == 0:
    cnt += (m[1] - s) // l
    e = m[1]
  else:
    cnt += (m[1] - s) // l + 1
    e = s + l * ((m[1] - s) // l + 1)
print(cnt)