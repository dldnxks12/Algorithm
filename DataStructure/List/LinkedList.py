'''
# 단순 연결 리스트 

 물리적인 순서 x 개념적 순서 O
 삭제, 삽입 연산 간단 (Linear List에 비해)
 
 Node : Data + Link
 
'''

# Node 생성

class Node():
  def __init__(self):
    self.data = None
    self.link = None


node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2 # Pointing Next Node Obj

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "문별"
node3.link = node4

node5 = Node()
node5.data = "사나"
node4.link = node5

# 문별과 사나 사이로 Node 삽입
newNode = Node()
newNode.data = "재남"
node4.link = newNode
newNode.link = node5

# 정연 Node 삭제 
node1.link = node3
del(node2)

# 모든 Node 순회하며 Data 출력 until Link None 
current = node1
print(current.data)
while current.link != None:
  current = current.link
  print(current.data)
  

# Linked List 함수로 구현

def printNodes(start):
  current = start
  if current == None:
    return 
  print(current.data, end ='')
  while current.link != None:
    current = current.link   # 다음 Node로 이동 
    print(current.data, end ='')
  print()  

#### Node 삽입
def inesrtNode(findData, insertData):
  global memory, head, pre, current 

  # 1. 첫 번째 Node로 삽입
  # 2. 중간 Node로 삽입
  # 3. 마지막 Node로 삽입

  # 1. 첫 번째 Node로 삽입
  if head.data == findData:
    node = Node() 
    node.data = insertData
    node.link = head
    head = node  # 해당 Node를 새로운 Head로 

  # 2. 중간 Node로 삽입
  current = head  # head 부터 순차적으로 
  while (current.data != None): 
    pre = current
    current = pre.link
    if (current.data == findData):
      node = Node()
      node.data = insertData
      pre.link = node
      node.link = current

  # 3. 마지막 Node로 삽입
  node = Node()
  node.data = insertData
  current.link = node
  

#### Node 삭제
def deleteNode(deleteData):
 gloabl memory , head, pre, current
 
 # 1. 첫 번째 Node 삭제
 # 2. 나머지 Node 삭제
   
 # 1. 첫 번째 Node 삭제
 if (head.data = deleteData):
  current = head
  head = current.link # 새로운 head로
  del(current) # 메모리에서 삭제 
   
 # 2. 나머지 Node 삭제 
 current = head
 while (current.data != None): # 삭제하려는 data가 있는 곳 까지 순회
  pre = current 
  current = current.link
  if( current.data == deleteData):
   pre.link = current.link
   del(current)


#### Node 검색

def findNode(findData):  
 
  current = head
  while(current.data != None):
   if(current.data == findData):
    return current # 현재 Node 반환
   else:    
   current = current.link   
  return None # 빈 Node 반환 
   
  
   
memory = []
head, pre, current = None, None, None # Linked List는 이전 노드로 돌아갈 수 없으므로, Head Node를 통해 재시작하도록 구현 

dataArray = ['다현' ,'쯔위' ,'문별' ,'재남', '사나']

if __name__ == "__main__" :

  node = Node()
  node.data = dataArray[0]
  head = node
  memory.append(node)

  for data in dataArray[1:]:
    pre = node    # 이전 Node 저장 
    node = Node() # Node 객체 생성 
    node.data = data
    pre.link = node
    memory.append(node)

  printNodes(head) # Head Node부터 순차적으로 시작 


  
