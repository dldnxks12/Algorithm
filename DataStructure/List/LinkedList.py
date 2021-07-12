# 물리적인 순서 x 개념적인 순서 

# Node 생성

class Node():
  def __init__(self):
    self.data = None
    self.link = None


node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "문별"
node3.link = node4

node5 = Node()
node5.data = "사나"
node4.link = node5

newNode = Node()
newNode.data = "재남"
node4.link = newNode
newNode.link = node5

node1.link = node3
del(node2)

current = node1
print(current.data)
while current.link != None:
  current = current.link
  print(current.data)
  

# Linked List 일반 구현
# p133

class Node():
  def __init__(self):
    self.data = None
    self.link = None

def printNodes(start):
  current = start
  if current == None:
    return 
  print(current.data, end ='')
  while current.link != None:
    current = current.link  
    print(current.data, end ='')
  print()

memory = []
head, pre, current = None, None, None

dataArray = ['다현' ,'쯔위' ,'문별' ,'재남', '사나']

if __name__ == "__main__" :

  node = Node()
  node.data = dataArray[0]
  head = node
  memory.append(node)

  for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

  printNodes(head)


  
