
'''
DFS(깊이 우선 검색) : 비선형 구조의 데이터 검색
    - Graph 완전 탐색 방법 
        - 종방향으로 탐색 
    - 모든 노드를 방문하고자 할 때 사용하는 방법

Stack을 이용해서 구현

방문하지 않는 Vertex : append로 push를 대체해서 사용
이미 방문한 Vertex   : pop
'''

class Graph():
    def __init__(self, size):
        self.size = size
        self.graph = [ [ 0 for _ in range(size)] for _ in range(size) ]


def GraphViewer(graph):
    print("Graph Viewer")

    for row in range(graph.size):
        for col in range(graph.size):
            print(graph.graph[row][col], end = ' ')
        print('')

def DFS(graph):

    stack = [] # Stack에 담았다 뺐다 하면서 방문 Vertex Check
    visitedVertex = [] # 방문 완료한 놈들 담을 list
    current = 0 

    stack.append(current)
    visitedVertex.append(current)

    while len(stack) != 0:
        next = None

        for vertex in range(graph.size):
            if graph.graph[current][vertex] != 0:  # connected
                if vertex in visitedVertex:
                    continue
                else:
                    next = vertex
                    break
        if next != None: # 해당 Vertex 담고 현재 Vertex로 설정 
            current = next
            stack.append(current)
            visitedVertex.append(current)
        else:
            current = stack.pop() # 되돌아가기

 
G = Graph(10)
GraphViewer(G)

##### 다시 ####

def DFSAgain(G):

    stack = []
    visitedVertex = []
    current = 0

    stack.append(current)
    visitedVertex.append(current)

    while len(stack) != 0:
        
        next = None
        for vertex in range(G.size):
            if G[current][vertex] in visitedVertex:
                continue
            else:
                next = vertex
        
        if next != None:
            current = next
            stack.append(current)
            visitedVertex.append(current)
        else:
            current = stack.pop()

