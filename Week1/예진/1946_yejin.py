import sys
input = sys.stdin.readline

T = int(input().rstrip())
for j in range(T):
  N = int(input().rstrip())
  grade = sorted([list(map(int, input().split())) for i in range(N)])
  cnt=1
  interviewWinner=grade[0][1]
  for i in range(1,N):
    if grade[i][1] < interviewWinner: #본인성적이 면접에선 이기는 경우
      interviewWinner = grade[i][1]
      cnt+=1
  print(cnt)

## 정렬하고
## 자기 윗사람들 중 면접성적 석차 젤 높은 사람만 보면된다.
## 왜? 일단 그사람에게 서류에서 밀린셈이니 면접에서 못이기면 -,-니까 탈락이다.