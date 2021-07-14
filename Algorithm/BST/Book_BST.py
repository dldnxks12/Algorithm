'''

도서관에 새로 입고된 책 정보를 이진 탐색 트리에 보관해서 검색 

책 이름과 작가 이름을 각각 이진 탐색 트리로 생성

'''

import random 

class TreeNode():
  def __init__(self):
    self.data = None
    self.left = None
    self.right = None
    
memory =  []
bookAry = [ ['어린왕자','생텍쥐베리'],['이방인','까뮈'],['부활','톨스토이'],['신곡','단테'],['돈키호테','세르반테스'],['동물농장','조지오웰'],['데미안','헤르만헤세'],['파우스트','괴테'],['대지','펄벅'] ]
random.shuffle(bookAry)

rootBook = None
rootAuthor = None

node = TreeNode()
node.data = bookAry[0][0]
rootBook = node
memory.append(node)

# Book Tree

for book in bookAry[1:]:
  node = TreeNode()
  name = book[0]
  node.data = name
  memory.append(node)

  current = rootBook 
  while True:
    if name < current.data:
      if current.left == None:
        current.left = node
        break
      else:
        current = current.left
    else:
      if current.right == None:
        current.right = node
        break
      else:
        current = current.right      
    memory.append(node)


print("Book tree Complete")

# Author tree

node = TreeNode()
node.data = bookAry[0][1]
rootAuthor = node
memory.append(node)

for book in bookAry[1:]:
  author = book[1]
  node = TreeNode()
  node.data = author
  
  current = rootAuthor

  while True:
    if author < current.data:
      if current.left == None:
        current.left = node
        break      
      else:
        current = current.left
      
    else:
      if current.right == None:
        current.right = node
        break
      else:
        current = current.right
        
    memory.append(node)

print("Author tree Complete")


bookOrAuthor = int(input('Book 1 Or Author 0 -->'))
findName = input("Book or Author-->")

if bookOrAuthor == 1:
  root = rootBook
else:
  root = rootAuthor

current = root

while True:
  if current.data == findName:
    print("Ok")
    break
  elif findName < current.data:
    if current.left == None:
      print("No data")
      break
    else:
      current = current.left 
  else:
    if current.right == None:
      print("No data")
      break
    else:
      current = current.right

