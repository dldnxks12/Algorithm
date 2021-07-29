'''

Circular List는 마지막 Node가 다시 Head를 가리키도록

'''

class Node():
    def __init__(self):
        self.node = None
        self.left = None
        self.right = None

def View():
    global head, memory, dataArr

    if head.node == None:
        return
    print(head.node, end = ' ')

    current = head
    for i in range(len(memory)):
        current = current.right
        if(current == last):
            print(current.node, end=' ')
            break
        print(current.node, end = ' ')


def Insertion(FindData, InsertData):
    global head, last, memory, dataArr
    node = Node()
    node.node = InsertData

    if head.node == FindData: # 첫 항?
        last.right = node
        head.left = node
        node.left = last
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
            current.left = node
            node.right = current
            node.left = pre
            memory.append(node)
            break
            return
        if current == last: # 마지막 항까지 봤는데 없다?
            current.right = node
            head.left = node
            node.right = head
            node.left = current
            node = last
            memory.append(node)
            break
            return

def delete(FindData):
    global head, last, memory, dataArr

    if head.node == FindData:
        next = head.right
        last.right = next
        next.left = last
        head.left, head.right, head.node = None, None, None
        del head
        head = next
        return

    current = head
    for _ in range(len(memory)):
        pre = current
        current = current.right
        if current == last:
            pre.right = head
            head.left = pre
            current.left, current.right, current.node = None, None, None
            del current
            break
            return
        next = current.right
        if current.node == FindData:
            pre.right = next
            next.left = pre
            current.left, current.right, current.node = None, None, None
            del current
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
    if i == dataArr[-1]:
        last = node
        pre.right = last
        last.left = pre
        last.right = head
        head.left = last
        break
    node.left = pre
    pre.right = node
    current = node

View()
Insertion('종수','똥')
print("")
View()
print("")
delete('친구')
View()


