import sys
sys.stdin=open("input.txt", "rt")

N , K = map(int, input().split())

devide = 0
count = 0
while devide <= N and count != K:
    devide = devide + 1
    if N % devide == 0 :
        count = count + 1
print(devide)
