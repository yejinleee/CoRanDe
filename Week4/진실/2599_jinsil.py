# 7. 짝 정하기(실3)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(3)]

def print_result():
	for i in range(0, arr[0][0]+1):
		AB = i 
		AC = arr[0][0]-i 
		BC = arr[2][1]-AC 
		BA = arr[1][0]-BC 
		CA = arr[0][1]-BA 
		CB = arr[2][0]-CA
		if AB >= 0 and AC >= 0 and BA >= 0 and BC >= 0 and CA >= 0 and CB >= 0:
			print(1)
			print(AB, AC)
			print(BA, BC)
			print(CA, CB)
			return
	print(0)
	return

print_result()



