'''

Binary Tree ---- Double Linked List로 구현 

Tree의 각 위치 : Node
위 노드와 바로 아래 노드 간 관계 : Parent ode <-> Child Node
Child Node 개수 : 차수 (Degree)
Degree = 0인 Node : Leaf Node

Root Node 부터 차례로 level 0 -> level 1 -> level 2 -> ...
Tree 의 차수는 가장 높은 차수를 기준으로 한다

* Computer는 0과 1로 표현하는 것에 최적화 되어있으므로 이진트리를 사용한다.

1. 포화 이진 트리 (Full Binary Tree)
  : All Node가 꽉찬 Tree 
  : Node 수 == 2^(높이+1)-1 
2. 완전 이진 트리 (Complete Binary Tree)
  : 일부분 비어있지만, 마지막 번호의 Node가 빈 Tree  
3. 편향 이진 트리 (Skewed Binary Tree)
  : All Node가 오른쪽이나 왼쪽으로 연결된 Tree

'''

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

print(node1.left.data, node1.right.data)

print(node2.left.data, node2.right.data)

print(node3.left.data)


