
'''

* 괄호 매칭 * 

1. 닫은 괄호 만났을 때 stack은 비어있지 않아야한다.
2. 닫는 괄호 만났을 때 추출한 괄호는 여는 괄호여야 한다.
3. 2를 만족하며 두 개의 괄호의 종류가 같아야 한다.
4. 모든 수식의 처리가 끝났을 때 Stack은 비어있어야한다.

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


def checkBracket(expr):

  Data = []
  for ch in expr:
    if ch == ('(' or '[' or '{' or '<' ):
      push(ch)
    elif ch == (')' or ']' or '}' or '>'):      
      data = pop()      
      if ch == ')' and data == '(':
        pass
      elif ch == '}' and data == '{':
        pass
      elif ch == ']' and data == '[':
        pass
      elif ch == '>' and data == '<':
        pass
      else:
        return False
      
  if isempty():
    return True
  else:
    return False
      
    
size = 100
stack = [None for _ in range(size)]
top = -1

if __name__ ==   "__main__":

  exprAry = ['(A+B)',')A+B(','((A+B)-C','(A+B]','(<A+{B-C}/[C*D]>)']

  for expr in exprAry:
    top = -1
    print(expr, '==>', checkBracket(expr))







