#push X: 정수 X를 스택에 넣는 연산이다.
#pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 스택에 들어있는 정수의 개수를 출력한다.
#empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
#top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
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
i = 0
while i < N :
  #command = input().split(" ")
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

  i = i + 1