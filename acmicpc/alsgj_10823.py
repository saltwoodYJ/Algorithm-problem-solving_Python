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
    last = stack[flag] # 마지막 값 저장
    del stack[flag] # 마지막 값 지우고
    flag = flag - 1 # 플래그 하나 감소
    print(last) # 지운 값 출력

def size() :
  global flag
  print(flag + 1)

def empty() :
  global flag
  if flag == -1 :
    print(1)
  else :
    print(0)

def top() :
  global flag
  if flag == -1 :
    print(-1)
  else :
    last = stack[flag]
    print(last)

#N = int(input())
N = int(sys.stdin.readline().strip())
for i in range(N) :
  command = sys.stdin.readline().strip().split()

  if command[0] == "push" :
    push(command[1])
  elif command[0] == "pop" :
    pop()
  elif command[0] == "size" :
    size()
  elif command[0] == "empty" :
    empty()
  elif command[0] == "top" :
    top()