'''

허니버터칩 재고가 가장 많은 편의점을 알아내려고 한다.

    -> DFS로 모두 Search 하여 가장 재고가 많은 편의점 이름 Find

'''

# Graph 생성
class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]

# Graph Viewer 생성
def GraphViewer(G):
    print("--Graph--")
    for row in range(G.SIZE):
        for col in range(G.SIZE):
            print(G.graph[row][col], end = ' ')
        print()

# Graph Search function 생성
def DFS(G, Stocks):

    stack = []
    visitedVertex = []
    current = 0
    Max_Stock = []

    stack.append(current)
    visitedVertex.append(current)
    Max_Stock.append(Stocks[current])

    while len(stack) != 0 :
        next = None 
        for vertex in range(G.SIZE):
            if G.graph[current][vertex] == 0:
                if vertex in visitedVertex:
                    continue
                else:
                    next = vertex
                    break
        if next != None:
            current = next
            stack.append(current)
            visitedVertex.append(current)
            Max_Stock.append(Stocks[current])
        else:
            current = stack.pop()

    MaxValue = max(Max_Stock)
    print(MaxValue)

    print("편의점 : ", MaxValue[1])

size = 5
G = Graph(size)

# GS 0 , CU 1, Sven11 2, MiniStop 3, Emart24 4

G.graph[0][1] = 1;G.graph[0][2] = 1
G.graph[1][0] = 1;G.graph[1][2] = 1;G.graph[1][3] = 1
G.graph[2][0] = 1;G.graph[2][1] = 1;G.graph[2][3] = 1
G.graph[3][1] = 1;G.graph[3][2] = 1;G.graph[3][4] = 1
G.graph[4][3] = 1

GraphViewer(G)

# Make Array for Stocks at Each Vertex [Stocks, VertexIndex]
Stocks = [[30,0],[60,1],[10,2],[90,3],[40,4]] 

DFS(G, Stocks)


