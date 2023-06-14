# 4. 놀라운 문자열(실3)

import sys
input = sys.stdin.readline

def isSur(string):
  for i in range(len(string)-2):
    arr = []
    for j in range(len(string)-1-i):
      arr.append(string[j]+string[j+i+1])
    if len(arr) != len(set(arr)): #중복이 있으면
      print(string, "is NOT surprising.")
      return
  print(string, "is surprising.")
  return

while True:
  string = input().rstrip()
  if string == '*':
    break

  if len(string) < 2:
    print(string, "is surprising.")
    continue
  isSur(string)
  


