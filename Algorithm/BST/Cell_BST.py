'''

2021 07 17 , P309 

1. 편의점에서 물건을 판매 
2. 판매하는 물건은 중복가능
3. 판매된 물건 종류를 살펴볼 때는 중복 x
4. BST를 이용


Todo
1. Binary Tree 생성
2. method 1. 순회를 통해 모두 출력 -> Set로 Type 변환 후 출력 
2. method 2. 검색 기능 구현 -> 팔린 물건 목록 모두 for문으로 던져서 검색 후 list에 담기 -> Set로 Type 변환 후 출력 

'''

import random


class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None        

def inorder(node): # Tree 생성 확인 
    if node == None:
        return
    else:
        print(node.data)
        inorder(node.left)
        inorder(node.right)
        return 
            

dataArray = ['바나나우유', '레쓰비', '츄파츕스', '도시락', '삼다수', '코카콜라', '삼각김밥']
SoldArray = [random.choice(dataArray) for _ in range(10)]

print("오늘 판매된 물건 --- " , SoldArray)

# ---- 구현 

memory = []
root = None

# --- Tree 생성

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
                current = current.left
        else:
            if current.right == None:
                current.right = node
                memory.append(node)
                break
            else:
                current = current.right

# -- Search 기능 구현

findlist = []

for data in SoldArray:

    current = root
    while True:
        if data == current.data:
            findlist.append(data)
            break
        elif data < current.data:
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

findlist = set(findlist)
print(findlist)














