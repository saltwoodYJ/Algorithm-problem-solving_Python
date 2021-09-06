def VPS(string) :
  stack = []
  for x in string :
    if x == "(" :
      stack.append("(")
    else :
      if stack :
        stack.pop()
      else :
        return "NO"
  if stack :
    return "NO"
  else :
    return "YES"

N = int(input())
for i in range(N):
  string = input()
  print(VPS(string))