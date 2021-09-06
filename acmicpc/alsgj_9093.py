stack = []

def main(string) :
  reverse_string = ""
  word = string.split() # 문장을 단어단위로 쪼개기
  for x in word :
    stack = list(x) # 단어를 알파벳 스택으로 만들고
    reverse = ""
    top = len(stack) - 1    
    while top != -1:
      reverse += stack[top]
      del stack[top]
      top = top - 1
    reverse_string += reverse
    if word.index(x) == len(word) - 1 : #마지막 단어라면 공백 안붙임
      continue
    else :
      reverse_string += " "
  print(reverse_string)

N = int(input())
for i in range(N) :
  string = input()
  main(string)