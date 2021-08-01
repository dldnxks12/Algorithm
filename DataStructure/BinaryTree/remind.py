class BinaryTree():
  def __init__(self):
    self.data  = None
    self.left  = None
    self.right = None

# BinaryTree 순회 -> 전위, 중위, 후위 

def preorder(node):

  if node == None:
    return 
  else:
    print(node.data)
    preorder(node.left)
    preorder(node.right)

def inorder(node):

  if node == None:
    return
  else:
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def postorder(node):

  if node == None:
    return 
  else:
    postorder(node.left)
    postorder(node.right)
    print(node.data)

# Binary Tree 삭제, 검색 

def Search(data):

  global root

  current = root
  while True:
    if current.data == data
      print("find")
      break
    elif data < current.data:
      if current.data == None:
        print("no")
        break
      current = current.left
    else:
      if current.data == None:
        print("no")
        break      
      current = current.right

  return 

def delete(data):

  global root

  current = root
  parent = None

  while True:
    if current.data == data:
      if current.left == None and current.right == None:
        if parent.left == current:
          parent.left = None
        else:
          parent.right = None
      elif current.left == None and current.right != None:
        if parent.left == current:
          parent.left = current.right
        else:
          parent.right = current.right
      elif current.left != None and current.right == None:
        if parent.left == current:
          parent.left = current.left
        else:
          parent.right = current.left
    elif current.data > data:
      if current.left == None:
        print("no")
        return
      else:
        parent = current
        current = current.left
    else:
      if current.right == None:
        print("no")
        return
      else:
        parent = current
        current = current.left
             
  

size = 100
memory = [None for _ in range(size)]
root = None
dataArray = ['블핑','레드벨벳','에이핑크','걸스데이','트와이스','마마무']

node = BinaryTree()
node.data = dataArray[0]
memory.append(node)
root = node

for data in dataArray[1:]:
  node = BinaryTree()
  node.data = data  
  current = root
  while True:
    if node.data < current.data:
      if current.left == None:
        current.left = node
        memory.append(node)
        break
      else:
        current = current.left
    else:
      if current.right = None:
        current.right = node
        memory.append(node)
        break
      else:
        current = current.right
