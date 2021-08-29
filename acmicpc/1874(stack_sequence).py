#  4, 3, 6, 8 ,7 ,5 ,2 ,1
import sys

top = -1
stack = []

N = int(sys.stdin.readline().strip())
i = 0
numb_list = []

while i < N :
  number = int(sys.stdin.readline().strip())
  numb_list.append(number)
  i = i + 1

factor = 1
for x in numb_list :
  while stack[top] != x :
    stack.append()