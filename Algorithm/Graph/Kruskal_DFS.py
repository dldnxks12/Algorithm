'''

# 신장 트리 : 최소 Edge로 모든 Vertex 연결
# 최소 신장 트리 : 신장 트리 중 최소 Weight
  - 신장 트리의 Edge 개수 = Vertex - 1
  
  - 최소 신장 트리 - Kruskal + DFS로 최소 비용 찾기 

'''

# Graph Class 정의
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

def printGraph(G):
  print("Adjacent Martrix")
  for row in range(G.SIZE):
    for col in range(G.SIZE):
      print(G.graph[row][col], end = ' ')
    print()

def FindVertex(G, findvertex):

    stack = []
    visitedArray = []
    current = 0

    stack.append(current)
    visitedArray.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(size):
            if G.graph[current][vertex] != 0:
                if vertex in visitedArray:
                    continue
                else:
                    next = vertex
                    break
        if next != None:
            current = next
            stack.append(current)
            visitedArray.append(current)
        else:
            current = stack.pop()

    for i in visitedArray:
        print(i, end = ' ') 

    if findvertex in visitedArray:
        print("연락 OK")
        return True
    else:
        print("연락 No")
        return False


# Graph 생성
    
size = 6
G = Graph(6)
G.graph[0][1] = 10;G.graph[0][2] = 15
G.graph[1][0] = 10;G.graph[1][2] = 40;G.graph[1][3] = 11;G.graph[1][4] = 50
G.graph[2][0] = 15;G.graph[2][1] = 40;G.graph[2][3] = 12
G.graph[3][1] = 11;G.graph[3][2] = 12;G.graph[3][4] = 20;G.graph[3][5] = 30
G.graph[4][1] = 50;G.graph[4][3] = 20;G.graph[4][5] = 25
G.graph[5][3] = 30;G.graph[5][4] = 25

# Graph 시각화 
printGraph(G)

# Weight, Start Vertex, End Vertex Array 생성 

edgeArray = []

for row in range(size):
    for col in range(size):
        if G.graph[row][col] != 0:
            edgeArray.append( [G.graph[row][col], row, col] )

print(edgeArray)

from operator import itemgetter

edgeArray = sorted(edgeArray, key = itemgetter(0), reverse=True)
newArray = []

for i in range(0, len(edgeArray), 2):
    newArray.append(edgeArray[i])

print(newArray)

# 최소 비용 신장 트리 생성

index = 0
while len(newArray)-1 > size-1:

    start = newArray[index][1]
    end   = newArray[index][2]
    saveWeight = newArray[index][0]

    G.graph[start][end] = 0
    G.graph[end][start] = 0

    if FindVertex(G,start) and FindVertex(G,end):        
        del newArray[index]    
    else:
        G.graph[start][end] = saveWeight
        G.graph[end][start] = saveWeight
        index += 1

printGraph(G)
    



    


    
    
    


