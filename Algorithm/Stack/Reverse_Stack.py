'''
# file 전체 줄 거꾸로
# file 글자도 모두 거꾸로

# ---> 1. file을 열고 읽어 들인 줄을 stack에 넣기 
# ---> 2. 읽어 들인 줄 또한 글자를 하나씩 나눠서 stack에 넣기 
# ---> 3. 다시 pop에서 write하기 
'''

def isfull():
  global size, top, stack

  if top == size - 1:
    return True
  else:
    return False

def isempty():
  global size, top, stack

  if top == -1:
    return True
  else:
    return False

def push(data):
  global size, top, stack

  if isfull():
    return 
  else:
    top += 1
    stack[top] = data    

def pop():
  global size, top, stack

  if isempty():
    return 
  else:
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek():
  global size, top, stack

  if isempty():
    return 
  else:
    return stack[top]

size = 100
top = -1
stack = [None for _ in range(size)]

if __name__ == "__main__":

  f = open("/content/drive/MyDrive/Colab Notebooks/Algorithm/new.txt", 'w')

  f.write("진달래꽃\n")
  f.write("나 보기가 역겨워\n")
  f.write("가실 때에는\n")
  f.write("말 없이 고이 보내드리오리다\n")

  f.close()


  f = open("/content/drive/MyDrive/Colab Notebooks/Algorithm/new.txt", 'r')

  lines = f.readlines()
  lines2 = []

  for line in lines:
    lines2.append(line[:-1])

  print(lines2)

  str = []
  for line in lines2:
    str1 = ""
    for ch in line:
      push(ch)
    for _ in line:
      str1 += pop()
    str1 += "\n"
    str.append(str1)


  print(str)

f = open("/content/drive/MyDrive/Colab Notebooks/Algorithm/new.txt2", 'w')

for i in str:
  f.write(i)
     
f = open("/content/drive/MyDrive/Colab Notebooks/Algorithm/new.txt2", 'r')

lines4 = f.readlines()
print(lines4) # check





