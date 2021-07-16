# Binary Tree Node 정의

class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right =None

# Binary Tree 생성, 순회, 삽입 , 삭제, 검색 기능 구현 

# 1. 순회 -- 전위 , 중위, 후위 (재귀 함수 사용)
def preorder(node):  # 중 -> 왼 -> 오  : 현재 노드 먼저 처리    
    if node == None:
        return
    else:
        print(node.data)        
        preorder(node.left)
        preorder(node.right)

def inorder(node):   # 왼 -> 중 -> 오   : 현재 노드 중간에 처리
    if node == None:
        return 
    else:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
    

def postorder(node): # 왼 -> 오 -> 중  : 현재 노드 마지막으로 처리
    if node == None:
        return 
    else:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


# Binary Tree 생성 및 삽입 

memory = []
root = None
dataArray = ['블핑','레드벨벳','에이핑크','걸스데이','트와이스','마마무']

node = TreeNode()
node.data = dataArray[0]
root = node 
memory.append(node)

    
for data in dataArray[1:]:    
    node = TreeNode()
    node.data = data
    current = root
    while True:
        if data < current.data:
            if current.left == None:
                current.left = node
                memory.append(node)
                break
            else:
                currnet = current.left
        else:
            if current.right == None:
                current.right = node
                memory.append(node)
                break
            else:
                current = current.right
        

# Binary Tree 검색 

'''

if 현재 노드 == Data -> 출력 

elif 현재 노드 > data -> 왼쪽 노드로 이동

else  현재 노드 <  data -> 오른쪽 노드로 이동 

'''

findName = '에이핑크'

current = root
while True:
    if findName == current:
        print("Found")
        break
    elif findName < current.data:
        current = current.left
    else:
        current = current.right

# Binary Tree 삭제 -> 조금 더 신경 써야함

'''
삭제한 Node 위치에 따라 3가지 상황으로 나눈다.
1. Leaf Node인 경우
2. 왼쪽 또는 오른쪽 Child Node가 있는 경우
3. 양쪽에 Child Node가 있는 경우 -> CH.10 재귀함수 때 다루자 

'''

deleteName = "마마무"
parent = None

current = root
while True:
    if deleteName == current.data:    
        if current.left == None and current.right == None: # leaf Node
            current.data = None 
            del current
            break
        elif current.left == None and current.right != None: # 오른쪽에 자식 노드 
            if parent.left == current: 
                parent.left = current.right
            else:
                parent.left = current.left
            del current            
            break
        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.left = current.left
            del current
            break
    elif deleteName > current.data:
        if current.right == None:
            print("Can't find data")
            break
        parent = current
        current = current.right
    else:
        if current.left == None:
            print("Can't find data")
            break            
        parent = current
        current = current.left




    

    





