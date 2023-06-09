import sys

N = int(sys.stdin.readline())
assignlist = []
sum = 0
for _ in range(N):
    assignment = list(map(int, sys.stdin.readline().split()))
    if assignment[0] == 1: #과제가 주어지면 바로 시작
        assignment[2] -= 1 #1분 줄어듦
        if assignment[2] == 0: #만약 다했다면
            sum += assignment[1] #과제 점수 더하기
            continue
        assignlist.append(assignment) #남은 과제 리스트에 추가
    else: #과제가 주어지지 않았다면
        if len(assignlist) > 0: #덜된 과제가 있다면
            assign = assignlist.pop() #가장 최근꺼 가져와서
            if assign[0] == 1: 
                assign[2] -= 1 #1분 줄어듦
            if assign[2] == 0: #만약 과제를 다했다면
                sum += assign[1] #과제 점수 더하기
                continue
            assignlist.append(assign) #남은 과제 리스트에 추가

print(sum) #총 과제 점수 출력