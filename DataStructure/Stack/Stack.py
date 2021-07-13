
'''

FILO 구조

1. Push : top + 1 -> data push
2. Pop  : data pop -> top -1 
3. stackisfull
4. stackisempty

* top은 -1에서 시작 (empty)
* top이 배열의 크기와 같을 때 (full)

'''

def isfull():
  global size, stack, top

  if top >= size-1:
    return True
  else:
    return False

def isempty():
  global size, stack, top

  if top == -1:
    return True
  else:
    return False

def push(data):
  global size, stack, top

  if isfull():
    return 
  else:
    top +=1 
    stack[top] = data      

def pop():
  global size, stack, top

  if isempty():
    return 
  else:
    data = stack[top]
    stack[top] = None
    top -=1
    return data 

def peek():
  global size, stack, top

  if isempty():
    return 
  else:
    return stack[top]
    

size = 5
stack = [None for _ in range(size)]
top = -1

