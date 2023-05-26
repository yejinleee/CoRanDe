# 6. 늑대와 양(실3)

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

# .을 모두 D로 바꾸기
for i in range(R):
	for j in range(C):
		if arr[i][j] == '.':
			arr[i][j] = 'D'

def check():
	#판에 양이 없을 때
	f = 0
	for i in range(R):
		if 'S' in arr[i]:
			f = 1
			break
	if f == 0:
		return 1

	#판에 양이 있을 때
	for i in range(R):
		for j in range(C):
			if arr[i][j] == 'S':
				if (i < R-1 and arr[i+1][j] == 'W') or (i > 0 and arr[i-1][j] == 'W') or (j < C-1 and arr[i][j+1] == 'W') or (j > 0 and arr[i][j-1] == 'W'):
					return 0
	return 1

#출력
print(check())
if check():
	for i in range(R):
		print(''.join(arr[i]))

