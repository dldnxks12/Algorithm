'''

Linked List는 끝까지 순회한 후 종료 -> Circuler List는 다시 Head로 return 
  -> 마지막 Node의 link가 head를 가리키도록 

1. Node 삽입
2. Node 삭제
3. Node 검색

'''


class Node():
  def __init__(self):
    self.data = None
    self.link = None

def printNode(start):
  current = start

  if (current.data == None):
    return
  print(current.data, end =' ')

  while (current.link != start):
    current = current.link
    print(current.data, end = ' ')

#***** 삽입 *****#
def insertNode(findData, insertData):
  global memory, head, pre, current

  # 첫 번째 Node에 삽입할 때 
  if (head.data == findData):
    node = Node()
    node.data = insertData
    node.link = current
    last = head
    while (last.link != head):
      last = last.link
    last.link = node
    head = node
    return 

  # 중간 노드 삽입
  current = head
  while (current.link != head):
    pre = current
    current = current.link
    if (current.data == findData):
      node = Node()
      node.data = insertData
      pre.link = node
      node.link = current
      return 

  # 마지막 노드 삽입
  node = Node()
  node.data = insertData
  current.link = node
  node.link = head  

#***** 삭제 *****#
def deleteNode(deleteData):
  global memory, head, pre, current

  # 첫 번째 노드 삭제
  if (head.data == deleteData):
    current = head
    head = head.link 
    while (current.link != current):
      current = current.link 
    current.link = head
    del (current)

  # 나머지 노드 삭제
  current = head
  while (current.link != head):
    pre = current
    current = current.link
    if (current.data == deleteData):
      pre.link = current.link
      del (current)


#***** 검색 *****#

def findNode(findData):

  global memory, head, pre, current
  
  current = head
  while (current.link != head):
    if ( current.data == findData):
      return current
    else:
      current = current.link

  return None

memory = []
head, pre, current = None, None, None
dataArray= ["다현","정연","쯔위",'사나','지효']

if __name__ == "__main__":

  node = Node()
  head = node
  node.data = dataArray[0]
  node.link = head
  memory.append(node)

  for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    node.link = head
    memory.append(node)

  printNode(head)

