import sys
input = sys.stdin.readline

n = int(input())

# 1
# 에라토스테네스의 체를 이용하여 n이상의 소수 목록 구하기 -> 그 중 펠린드롬인 수 구하기
## 41756 KB / 192 ms

# '에라토스테니스의 체' 란?
## 소수를 판별하는 방식
## 나열 된 자연수들 중 2부터 시작하여 그의 배수들을 지워가며 마지막에 남은 수, 소수들을 찾는다.
## 1은 소수가 아니다.

def prime_list(n):
    primeTF = [True] * 1003002 
    # 콘솔을 찍어본 결과, 1000000이상인 가장 작은 소수이며 팰린드롬인 숫자는 1003001 이다.
    primeTF[1] = False # 1은 소수가 아니다.

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(1000000 ** 0.5)
    for i in range(2, m+1):
        if primeTF[i] == True: # 소수인 경우
            for j in range(i+i, 1003002, i): # i이후 i의 배수들은 False
                primeTF[j] = False

    return [i for i in range(n, 1003002) if primeTF[i] == True]

prime = prime_list(n)

def palindrome(n):
    strn = str(n)
    l = len(str(n))
    for i in range(0,l//2):
        if strn[i] != strn[l-i-1]:
            return False
    return True

for p in prime:
    if palindrome(p):
        print(p)
        break


'''
# 2
## 제곱근까지 나눠가며 소수 판별하기 -> 그 수가 펠린드롬인지 확인
## 31256KB / 552 ms

def isPrime(i):
    if i==1: return False
    for j in range(2, int(i ** 0.5 )+1):
        if i % j ==0: return False
    return True

def palindrome(n):
    strn = str(n)
    l = len(str(n))
    for i in range(0,l//2):
        if strn[i] != strn[l-i-1]:
            return False
    return True



while True:
    if palindrome(n):
        if isPrime(n):
            print(n)
            break
    n+=1

'''
