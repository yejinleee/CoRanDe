# 19. 잃어버린 괄호(실2) 맞음

M = input()

# '-' 기준으로 문자열 나누기
math = M.split('-')

# '+' 기준으로 또 나누기 
# math2는 2차원 리스트가 됨
math2 = []
for i in math :
  math2.append(list(map(int, i.split('+'))))

# math2 각 리스트의 합을 math3에 저장
math3 = []
for i in math2 :
  math3.append(sum(i))

# 첫 번째 수에서 뒤에 수들을 다 빼준다
result = math3[0]
for i in range (1, len(math3)) :
  result -= math3[i]

print(result)