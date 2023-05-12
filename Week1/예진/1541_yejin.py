import sys
formula = sys.stdin.readline().rstrip().split('-')

final =[]
for i in formula:
  li = i.split('+')
  sum=0
  for j in li:
    sum+=int(j)
  final.append(sum)

result = final[0]
for i in final[1:]:
  result-=i
print(result)
