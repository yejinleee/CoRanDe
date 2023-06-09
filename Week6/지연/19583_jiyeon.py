import sys

S, E, Q = sys.stdin.readline().split()
stime = S.split(":")
start = int(stime[0])*60 + int(stime[1]) #시간 입력받은거 다 분으로 치환
etime = E.split(":")
end = int(etime[0])*60 + int(etime[1])
qtime = Q.split(":")
quit = int(qtime[0])*60 + int(qtime[1])

std = dict() #출석명단 체크
ans = dict() #끝날때 명단 체크
while True:
    try: #엔터처리를 하기 위해서 try except구문 사용
        time, nickname = sys.stdin.readline().strip().split()
        ttime = time.split(":")
        t = int(ttime[0])*60 + int(ttime[1]) #이 시간도 마찬가지로 분으로 치환
        if t <= start: #만약에 개강총회 시작시간까지 채팅쳤으면
            std[nickname] = 1 #명단 체크
        if end <= t <= quit: #개강총회 끝나고 스트리밍 끝나는시간까지 채팅쳤으면
            if nickname in std: #그 채팅친 사람이 명단에 있으면 체크
                if nickname not in ans: #중복 처리용
                    ans[nickname] = 1
    except:
        break
print(len(ans)) #학생 명수 출력