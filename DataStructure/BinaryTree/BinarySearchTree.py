'''

** Binary Search Tree를 구현하는 방법은 두 가지
1. 재귀 함수 2. Stack 

  -> 재귀 함수를 이용하는 것이 훨씬 간편 

1. 전위 순회 Preorder Search -- 노드의 데이터를 먼저 처리

  - 현재 노드 데이터 처리
  - 왼쪽 서브 트리로 이동
  - 오른쪽 서브 트리로 이동 

2. 중위 순회 Inorder Search  -- 노드의 데이터를 중간에 처리

  - 왼쪽 서브 트리로 이동
  - 현재 노드 데이터 처리  
  - 오른쪽 서브 트리로 이동 

3. 후위 순회 Postorder Search -- 노드의 데이터를 마지막에 처리

  - 왼쪽 서브 트리로 이동
  - 오른쪽 서브 트리로 이동 
  - 현재 노드 데이터 처리

'''

# Binary Search Tree

class TreeNode():
  def __init__(self):
    self.data  = None
    self.left  = None
    self.right = None


node1 = TreeNode()
node1.data = "화사"

node2 = TreeNode()
node2.data = "솔라"
node3 = TreeNode()
node3.data = "문별"

node1.left = node2
node1.right = node3

node4 = TreeNode()
node4.data = "휘인"
node5 = TreeNode()
node5.data = "쯔위"

node2.left = node4
node2.right = node5

node6 = TreeNode()
node6.data = "선미"

node3.left = node6

def preorder(node):
  if node == None:
    return 
  else:
    print(node.data, end = '->')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
  if node == None:
    return
  else:
    inorder(node.left)
    print(node.data, end = '->')
    inorder(node.right)

def postorder(node):
  if node == None:
    return 
  else:
    postorder(node.left)
    postorder(node.right)  
    print(node.data, end = '->')

print("전위 순회", preorder(node1))
print("중위 순회", inorder(node1))
print("후위 순회", postorder(node1))

