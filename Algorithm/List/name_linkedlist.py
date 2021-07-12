'''

# 명함 관리 프로그램 

이름과 연락처를 무작위로 입력 -> 이름 순서대로 linked list에 저장 

'''

# Node 정의
class Node():
  def __init__(self):
    self.data = None
    self.link = None

# Linked list의 삽입 삭제 함수 

def insert(insertData):

  global memory, head, pre, current  
  # 첫 번째 노드, 중간 노드, 마지막 노드

  node = Node()
  node.data = insertData
  memory.append(node)
  

  # 1. 첫 번째 노드
  if (head == None):
    head = node
    return 

  if (head.data[0] > insertData[0]):
    node.link = head
    head = node
    return 

  # 2. 중간 노드
  current = head
  while (current.link != None):
    pre = current
    current = current.link 
    if (current.data[0] > insertData[0]):
      pre.link = node
      node.link = current 
      return 

  # 3. 마지막 노드
  current.link = node
    
def delete(deleteData):

  global memory, head, pre, current  

  # 첫 번째 노드, 이외의 노드
  if (head.data == deleteData):
    current = head
    head = current.link
    del(current)
    return 

  current = head
  while (current.data != Node):
    pre = current
    current = current.link
    if (current.data == deleteData):
      pre.link = current.link
      del(current)
      return

def findNode(findData):

  global memory, head, pre, current  

  current = head
  while (current.data != None):    
    if (current.data == findData):
      return current
    else:      
      current = current.link
  return None


def printNode(start):
  
  current = start

  if current == None:
    return 

  print(current.data , end = ' ')

  while (current.link != None):  
    current = current.link 
    print(current.data , end = ' ')


dataArray = [ ['지민', '010-1111-1111'], ['정국', '010-2222-2222'], ['슈가', '010-3333-3333'], ['뷔', '010-4444-4444']]

memory = []
head, pre, current = None, None, None

if __name__ == "__main__":

  for i in dataArray:
    insert(i)

printNode(head)




