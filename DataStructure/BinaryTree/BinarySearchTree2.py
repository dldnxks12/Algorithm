'''

BST의 일반구현

1. Tree 생성
2. 검색
3. 삭제 

'''

class TreeNode():
  def __init__(self):
    self.data = None
    self.left = None
    self.right = None

memory = []
root = None
nameAry = ["블랙핑크",'마마무','레드벨벳','에이핑크','걸스데이','트와이스']

if __name__ == "__main__":


  # -------------------------- Tree 생성 
  node = TreeNode()
  node.data = nameAry[0]
  root = node
  memory.append(node)

  for name in nameAry[1:]:

    node = TreeNode()
    node.data = name

    current = root

    while True:
      if current.data < name : # 왼쪽 Sub Tree      
        if current.left == None:
          current.left = node
          break
        current = current.left
      else:
        if current.right == None:
          current.right = node
          break
        current = current.right 

    memory.append(node)

  print("BST Ok")

  # -------------------------- Search 

  findName = "마마무"
  current = root    

  while True:  
    if current.data == findName:
      print("Find Here")
      break
    elif current.data < findName: 
      if current.data == None:
        print("Cant Find")
        break
      current = current.left       
    else :
      if current.data == None:
        print("Cant Find")
        break      
      current = current.right      

  # ---------------------------  Delete 
  deleteName = "마마무"      

  current = root
  parent = None
  while True:
    if current.data == deleteName:
      if current.left == None and current.right == None:
        if parent.left == current:
          parent.left = None
        else:
          parent.right = None
        print("삭제 ok")
        del current
        break
      
    elif current.left != None and current.right == None:
      if parent.left == current:
        parent.left = current.left
      else:
        parent.right = current.left 
      print("삭제 ok")
      del current 
      break

    elif current.left == None and current.right != None:
      if parent.left == current:
        parent.left = current.right
      else:
        parent.right = current.right       
      print("삭제 ok")
      del current 
      break
      
    elif deleteName > current.data:
      if current.left == None:
        print("No data in Tree")
        break
      else:
        parent = current 
        current = current.right
    else:
      if current.data == None:
        print("No data in Tree")
        break
      else:
        parent = current 
        current = current.left        

        
