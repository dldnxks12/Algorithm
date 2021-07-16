# Remind Binary Tree

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
    





