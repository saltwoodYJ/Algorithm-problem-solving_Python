import sys

stack = []
string = "(())())"

def VPS(string) :
  top = -1
  for x in string :
    if x == "(" :
      stack.append("(")
      top = top + 1
    elif x == ")" :
      if top == -1 :
        return "NO"
      del stack[top]
      top = top - 1
    print(stack)
  if top == -1 :
    return "YES"
  else :
    return "NO"

N = int(sys.stdin.readline().strip())
i = 0
while i < N :
  string = sys.stdin.readline().strip()
  print(VPS(string))
  i = i + 1