#  4, 3, 6, 8 ,7 ,5 ,2 ,1
import sys


N = int(sys.stdin.readline().strip())
i = 0
numb_list = []

def sequence(numb) :
  number = 1
  stack = []
  pp = []

  for x in numb :
    if len(stack) <= 0 :
      while number != x+1 :
        stack.append(number)
        number = number + 1
        pp.append('+')
      stack.pop(-1)
      pp.append('-')
      continue
    if stack[-1] == x :
      stack.pop(-1)
      pp.append('-')
    elif stack[-1] < x :
      while stack[-1] != x :
        stack.append(number)
        number = number + 1
        pp.append('+')
      stack.pop(-1)
      pp.append('-')
    elif stack[-1] > x :
      print("NO")
      return 0
  
  for x in pp :
    print(x)
    

while i < N :
  number = int(sys.stdin.readline().strip())
  numb_list.append(number)
  i = i + 1

sequence(numb_list)