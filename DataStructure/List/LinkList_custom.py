# single list

# 1. 삽입 - 맨 앞 , 맨 뒤, 중간
# 2. 삭제 - 맨 앞 , 맨 뒤 , 중강
# 3. 검색 - Sequential Search

class Node():
    def __init__(self):
        self.node = None
        self.link = None

def Insertion(node,finddata): # 삽입할 Node, i th node

    global data, head, memory
    if head.node == finddata: # 맨 앞
        node.link = head
        head = node
        return

    current = head
    for _ in range(len(memory)):
        pre = current
        current = current.link
        if current.node == finddata:
            pre.link = node
            node.link = current
            break

        if current.link == None:  # 마지막까지 없다면 -> 마지막 노드에 추가
            current.link = node
            break
    return

def delate(findata):
    global data, head, memory

    if head.node == findata:
        next = head.link
        head.node = None
        head.link = None
        del (head)
        head = next
        return

    current = head
    for _ in range(len(memory)):
        pre = current
        current = current.link
        next= current.link
        if current.node == findata:
            pre.link = next
            current.link = None
            current.node = None
            del( current )
            break
        if next == None: # 마지막 node
            current.node = None
            del (current)
            break
    return




def SequentialSearch(head): # head에서 끝까지 (link == None까지)

    global data

    if head.node == None:
        return
    print(head.node, end = ' ')

    current = head
    for _ in range(len(data)):
        current = current.link
        print(current.node, end = ' ')
        if current.link == None:
            break
    return

data = ["종수",'가영','친구']
head = None # head node
memory = []
node = Node()
head = node
node.node = data[0]
memory.append(node)

current = node
for i in data[1:]:
    pre = node # 이전 노드 저장
    node = Node()
    memory.append(node)
    node.node = i
    pre.link = node
    pre = node

SequentialSearch(head)
print('')
node_ = Node()
node_.node = "수진"


