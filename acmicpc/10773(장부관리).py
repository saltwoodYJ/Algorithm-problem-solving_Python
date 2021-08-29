#백준 10773번
#첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
#이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
#정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

import sys

stack = []
flag = -1

def push(value) :
  global flag
  stack.append(value)
  flag = flag + 1

def pop() :
  global flag
  if stack == [] : # 비어있으면 -1 출력
    print(-1)
  else :
    del stack[flag] # 마지막 값 지우고
    flag = flag - 1 # 플래그 하나 감소

#N = int(input())
N = int(sys.stdin.readline().strip())
i = 0
while i < N :
  #command = input().split(" ")
  number = int(sys.stdin.readline().strip())

  if number == 0 :
    pop()
  else :
    push(number)

  i = i + 1

total = 0
for x in stack :
  total = total + x
print(total)