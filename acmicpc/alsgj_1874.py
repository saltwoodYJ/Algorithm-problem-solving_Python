# 8 4 3 6 8 7 5 2 1 
import sys

N = int(sys.stdin.readline().strip())
numb_list = []    
for i in range(N) :
  number = int(sys.stdin.readline().strip())
  numb_list.append(number)

def sequence(numb) :
  number = 1
  stack = []
  sign = []

  for x in numb :
    while number <= x :
      stack.append(number)
      sign.append('+')
      number += 1
      print(stack)
    if stack[-1] == x :
      stack.pop(-1)
      sign.append('-')
  
    elif stack[-1] > x : #스택수열 성립안됨 NO 프린트후 종료
      print("NO")
      return 0
  
  for x in sign :
    print(x)

sequence(numb_list)