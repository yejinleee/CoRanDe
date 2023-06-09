import sys

while True:
    string = list(sys.stdin.readline().strip())
    if string[0] == "*":
        break
    if len(string) == 1: #한글자는 당연히 놀라운 문자열이니까 출력하고 넘어감
        print(*string, "is surprising.")
        continue
    flag = 1 #분기처리 조건 변수(놀라운 문자열이 아닐 경우 빠르게 처리하기 위함)
    for i in range(1, len(string)):
        ans = []
        for j in range(0, len(string)-i): #문자열 슬라이싱
            s = string[j]+string[j+i]
            if s in ans: #만약 문자열이 있으면
                flag = 0 #놀라운문자열이 아니라고 체크
                break
            ans.append(s)
        if flag == 0: #만약 놀라운 문자열이 아니면 뒤를 더 볼 필요가 없으니까 출력하고 넘어감
            print(''.join(string), "is NOT surprising.")
            break
    if flag: #빠져나온게 놀라운 문자열이면 출력
        print(''.join(string), "is surprising.")