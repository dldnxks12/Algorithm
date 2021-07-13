'''

1. 1~100 사이 숫자 7개 뽑기 (중복 허용) 
2. 순서대로 Circular List 구성
3. Head부터 순차적으로 돌며 짝수, 홀수 개수 파악
4. 둘 중 많은 것을 음수로 변경 

----- Circular list의 삽입 연산과 검색 연산 필요 ----

'''

import random

class Node():
  def __init__(self):
    self.data = None
    self.link = None

def printNode(start):
  current = start
  if (current.data == None):
    return
  print(current.data , end = ' ')

  while (current.link != start):        
    current = current.link
    print(current.data , end = ' ')
  print()

def InsertData(number):

  global memory, head, pre, current 

  node = Node()
  node.data = number

  # 새로 들어온 수가 첫 번째 수 보다 더 작다면 -- logic ok 
  if (head.data > number):
    node.link = head    
    current = head
    while (current.link != head):
      current = current.link
    current.link = node
    head = node
    return

  # 중간 노드로 삽입 -- logic ok 
  current = head 
  while (current.link != head):
    pre = current
    current = current.link
    if (current.data > number): 
      pre.link = node
      node.link = current 
      return

  # 마지막 노드로 삽입
  current.link = node
  node.link = head
  return 


# 짝수 홀수 Count
def Odd_Even():

  global memory, head, pre, current, odd, even, odd_flag 
  current = head
  while (current.link != head):
    if (current.data % 2 == 0 ):
      even +=1
    else:
      odd +=1
    current = current.link   

  if odd > even:
    odd_flag = 1
  else:
    odd_flag = 0
  
  if (odd_flag == 1):
    current = head
    while (current.link != head):
      if (current.data % 2 != 0 ):
        current.data = current.data*(-1)
      current = current.link   
  else:
    current = head
    while (current.link != head):
      if (current.data % 2 == 0 ):
        current.data = current.data*(-1)
      current = current.link   
      
memory = []
head, pre, current = None, None, None
odd_flag = 0

if __name__ == "__main__":

  odd,even = 0 , 0 

  dataArray= []
  for _ in range(7):
    dataArray.append(random.randint(1,100))

  print(dataArray)

  node = Node()
  node.data = dataArray[0]  
  head = node
  node.link = head
  memory.append(node)

  for data in dataArray[1:]:
    InsertData(data)

  printNode(head)  
  Odd_Even()

  print("Odd {} , Even {}".format(odd,even))

  printNode(head)  

