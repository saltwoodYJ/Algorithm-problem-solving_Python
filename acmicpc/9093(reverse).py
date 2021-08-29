import sys

stack = []

def main(string) :
  reverse_string = ""
  word = string.split()
  for x in word :
    stack = list(x)
    reverse = ""
    top = len(stack) - 1
    
    while top != -1:
      reverse = reverse + stack[top]
      del stack[top]
      top = top - 1
    reverse_string = reverse_string + reverse
    if word.index(x) == len(word) - 1 :
      continue
    else :
      reverse_string = reverse_string + " "
  print(reverse_string)

N = int(sys.stdin.readline().strip())
i = 0
while i < N :
  string = sys.stdin.readline().strip()
  main(string)
  i = i + 1