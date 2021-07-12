'''
# 1~45 까지 숫자 6개 랜덤 뽑기
  
  뽑은 숫자는 순서대로 단순 연결 리스트로 저장
  
'''
import random

class Node():
  def __init__(self):
    self.data = None
    self.link = None

def printNode(start):
  current = start

  if (current == None):
    return
  print(current.data , end = ' ')

  while (current.link != None):
    current = current.link
    print(current.data , end = ' ')  

  print()


def insert(number):

  global memory, head, pre, current 

  node = Node()
  node.data = number
  memory.append(node)
  
  # Link list가 처음 생성된 것이라면 
  if (head == None):
    head = node
    return 

  # 새로 들어온 number가 head보다 작다면 
  if (head.data > node.data):
    current = head
    head = node 
    head.link = current 
    return 

  # 중간에 삽입
  current = head
  while (current.link != None):
    pre = current
    current = current.link
    if (current.data > node.data):
      pre.link = node
      node.link = current
      return 

  # 마지막에 삽입
  current.link = node

if __name__ == "__main__":

  nums = range(45)

  memory = []
  head, pre, current = None, None, None

  count = 0

  while (count < 7):
    ran = random.randint(1,45)
    insert(ran)
    count +=1

  printNode(head)

