import sys
input = sys.stdin.readline

t = int(input())
#2
def checkPaper(n, paper):
  start = n-1 #처음 중간인 인덱스
  for i in range(start,len(paper),n):
    if paper[i-(n//2)]+paper[i+(n//2)] !=1:
      return 'NO'

for _ in range(t):
  paper = [int(i) for i in input().rstrip()]
  prtYN = 'YES'
  if len(paper)!=1:
    n=2
    while n<len(paper):
      if checkPaper(n, paper)=='NO':
        prtYN='NO'
        break
      n*=2
  print(prtYN)

'''
안으로 접힌 경우 그다음도 안으로 접으면 001
안으로 접힌 경우 그다음은 밖으로 접으면 100
밖으로 접힌 경우 그다음도 밖으로 접으면 110
밖으로 접힌 경우 그다음은 안으로 접으면 010

#1 가운데 부터 시작해서 이진탐색처럼 양쪽을 반갈라 가면서 확인
#2 오히려 젤 마지막 부터 시작해서 +2씩 뛰며 검사, +4씩 뛰며, +8씩 ... <-시간이 이게 더 빠를까?
'''