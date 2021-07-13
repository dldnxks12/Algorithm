'''

양방향으로 연결되는 링크 간단하게 생성 

--- 삽입, 삭제, 연산 x --- 

'''

class Node():
  def __init__(self):
    self.plink = None
    self.nlink = None
    self.data  = None

def printNode(start):
  current = start
  if current == None:
    return
  print(current.data, end = ' ')
  
  while current.nlink != None:
    current = current.nlink
    print(current.data, end = ' ')
  print()

  print(current.data, end = ' ')
  while current.plink != head:
    current = current.plink
    print(current.data, end = ' ')
  print(current.data, end = ' ')

  print()

memory = []
head, pre, current= None, None, None

dataArray = ["다현", "정연","쯔위","사나","지효"]

if __name__ == "__main__":

  node = Node()  
  node.data = dataArray[0]
  head = node
  memory.append(node)

  
  for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.nlink = node
    node.plink = pre
    memory.append(node)
    
printNode(head)

'''

---정방향---
다현 정연 쯔위 사나 지효 

---역방향---
지효 사나 쯔위 정연 정연 

'''

