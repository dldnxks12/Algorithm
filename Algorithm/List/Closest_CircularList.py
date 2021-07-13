'''

현재 위치를 (0,0) 이라 할 때, 편의점 위치 (x , y)와 가장 가까운 순서대로 Circular List 생성

1. 편의점 10개를 A,B,C, ... 순서로 
2. 위치 x,y는 1~100 까지 랜덤한 좌표
3. 현재 위치와 편의점 거리는 유클라디안 거리
4. 편의점 1개 Data는 (편의점 이름, x좌표, y좌표)의 tuple로 구성

'''

import random
import math


class Node():
  def __init__(self):
    self.data = None
    self.link = None

def printNode(start):
  current = start
  
  if current.data == None:
    return
  print(current.data , end =' ')

  while current.link != start:
    current = current.link
    print(current.data , end =' ')    
  print()

def Euclidean(Pos):
  distance = math.sqrt((Pos[1]**2) + (Pos[2]**2))
  return distance

def InsertNode(data):  
  global memory, head, pre, current

  node = Node()
  node.data = data[0:3] 
  memory.append(node)

  # 들어온 data의 거리가 head 거리보다 작다면 새 Node를 head로 
  if (head.data[2] > data[3]) : 
    node.link = head
    last = head
    while (last.link != head):
      last = last.link
    last.link = node
    head = node
    return 

  current = head
  while current.link != head:
    pre = current 
    current = current.link
    if current.data[2] > data[3]:
      pre.link = node
      node.link = current
      return 
    
  current.link = node
  node.link = head
  return 
  

memory = []
head, pre, current = None, None, None
position = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] # 10개 지점
dataArray = []

for data in position:
  dataArray.append( (data, random.randint(1,100), random.randint(1,100)))

distance = []  

for data in dataArray:
  dis = Euclidean(data)
  distance.append(dis)

Data = []

for data,dis in zip(dataArray, distance) :
  data = list(data)
  data.append(dis)
  data = tuple(data)  
  Data.append(data)
  
if __name__ == "__main__":

  # Head Node 생성 
  node = Node()
  node.data = Data[0][0:3]
  head = node
  node.link = head
  memory.append(node)

  for data in Data[1:]:
    InsertNode(data)
  
print(Data)
print(distance)
printNode(head)

'''

[('A', 3, 41, 41.10960958218893), ('B', 49, 17, 51.86520991955976), ('C', 11, 50, 51.19570294468082), ('D', 96, 90, 131.59027319676784), ('E', 34, 3, 34.132096331752024), ('F', 54, 80, 96.51942809610924), ('G', 62, 32, 69.77105417004964), ('H', 41, 16, 44.01136216933077), ('I', 77, 88, 116.93160394008115), ('J', 59, 50, 77.33692520394123)]
[41.10960958218893, 51.86520991955976, 51.19570294468082, 131.59027319676784, 34.132096331752024, 96.51942809610924, 69.77105417004964, 44.01136216933077, 116.93160394008115, 77.33692520394123]

('E', 34, 3) ('A', 3, 41) ('B', 49, 17) ('H', 41, 16) ('C', 11, 50) ('G', 62, 32) ('J', 59, 50) ('D', 96, 90) ('F', 54, 80) ('I', 77, 88) 


Path : E -> A -> B -> H -> C -> G -> J -> D -> F -> I

'''
  
    
