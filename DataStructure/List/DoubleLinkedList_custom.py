# double list -> 앞과 뒤 모두 link 존재
# double list를 왜 쓰냐? 앞으로 뒤로 움직일 수 있도록 하기 위함


class Node():
    def __init__(self):
        self.node = None
        self.left = None # 왼쪽 node
        self.right = None # 오른쪽 node

def View():
    global memory, head
    if head.node == None:
        return
    print(head.node, end = ' ')

    current = head
    for _ in range(len(memory)):
        current = current.right
        print(current.node , end = ' ')
        if current.right == None:
            break
            return

def Insertion(FindData, InsertData):
    global memory, head, dataArr

    node = Node()
    node.node = InsertData

    if head.node == FindData:
        head.left = node
        node.right = head
        head = node
        memory.append(node)
        return

    current = head
    for _ in range(len(memory)):
        pre = current
        current = current.right
        if current.node == FindData:
            pre.right = node
            node.left = pre
            current.left = node
            node.right = current
            memory.append(node)
            break
            return
        if current.right == None:
            current.right = node
            node.left = current
            memory.append(node)
            break
            return

def delete(finddata):

    global head, memory, dataArr
    if head.node == finddata:
        next = head.right
        next.left = None
        head.right = None
        head.node = None
        del head
        head = next
        return

    current = head
    for _ in range(len(memory)):
        pre = current
        current = current.right
        if current.right == None:
            pre.right = None
            current.left = None
            current.node = None
            del (current)
            break
            return
        next = current.right
        if  current.node == finddata:
            pre.right = next
            next.left = pre
            current.left = None
            current.right = None
            current.node = None
            del (current)
            break
            return

memory = []
dataArr = ["종수",'가영','수진','친구']
head = None

node = Node()
node.node = dataArr[0]
node.left = None
head = node
memory.append(node)

current = head
for i in dataArr[1:]:
    pre = current
    node = Node()
    node.node = i
    memory.append(node)
    pre.right = node
    node.left = pre
    current = node

View()

Insertion("친구", "진구")
print("")
View()
delete("친구")
print("")
View()
