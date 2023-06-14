# 9. 싸이버개강총회(실2)
# pypy3로 통과

# 입력
S, E, Q = map(str, input().split())
s = list(map(int, S.split(':')))
e = list(map(int, E.split(':')))
q = list(map(int, Q.split(':')))
start = s[0]*60 + s[1]
end = e[0]*60 + e[1]
qna = q[0]*60 + q[1]

checkin = set() #시간초과 해결
checkout = set()
while True:
  try:
    ti, person = map(str, input().split())
    t = list(map(int, ti.split(':')))
    time = t[0]*60 + t[1]
    if time <= start:
      checkin.add(person)
    elif end <= time <= qna:
      checkout.add(person)
  except:
    break

result = 0
for i in checkin:
  if i in checkout:
    result += 1
print(result)