# stack -> 1. 괄호 짝 맞추기 2. Palindrome

# palindrome - 앞으로 읽으나 뒤로 읽으나 같은 문자 검사

def push(data):

  global stack, size, top

  if top == size-1:
    print("Stack is Full")
    return 
  
  top = top+1
  print(top)
  stack[top] = data
  return 

def pop():

  global stack, size, top

  if top == -1:
    print("Stack is Empty")
    return 
  
  data = stack[top]
  stack[top] = None
  top = top -1
  return data 

size = 100
top = -1
stack = [None for _ in range(size)]

Sample = ["reverse", "ara", "banana", "sksks"]

for i in Sample:
  for k in i:
    push(k)
  for k in i:
    data = pop()
    
    if k == data:
     continue
    else:
      print(i+"is not palindrome")
      break
