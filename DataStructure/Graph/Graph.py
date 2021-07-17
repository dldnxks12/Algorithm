'''
Graph : 여러 Node가 서로 연결된 구조 

Node = Vertex 
Line = Edge 

- Edge의 방향성 유무에 따라 
    1. 방향 그래프 2. 무방향 그래프 + 3. 가중치 그래프 

- G1 Graph의 Vertex , Edge
    Vertex : V(G1) = {A, B, C, D}
    Edge : E(G1) = {(A,B),(B,C),(C,D)} : 무방향
    Edge : E(G1) = {<A,B>,<B,C>,<C,D>,<B,A>,<C,B>,<D,C>} : 방향 

    + Weighted Graph : Edge 간의 가중치 존재

- Graph 순회
    1. DFS - Depth First Search
    2. BFS - Breadth Firse Search``
`
- Graph의 표현
    Adjacent Matrix 이용

# DFS -> Stack 으로 구현     
    방문한 Vertex -> Stack에 Push  .append로 구현
    방문할 Vertex가 막다른 곳 -> Stack에서 Pop
    And 기존에 방문하였는지 여부를 확인하고자 방문했던 기록을 배열에 저장


'''

# Graph 생성

class Graph():
    def __init__(self, size):
        self.SIZE = size    
        self.graph = [[0 for _ in range(size)] for _ in range(size)] # 2차원 배열 생성


size = 4
G1 = Graph(size)

G1.graph[0][2] = 1;G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1;G1.graph[2][1] = 1;G1.graph[2][3] = 1
G1.graph[3][0] = 1;G1.graph[3][2] = 1

for rows in range(size):
    for cols in range(size):
        print(G1.graph[rows][cols], end = ' ')
    print()


current = 0 # Vertex A
stack = []
visitedArray = []

# A Vertex 입장

stack.append(current)
visitedArray.append(current)

while len(stack) != 0:
    next = None 
    for vertex in range(size):
        if G1.graph[current][vertex] == 1:
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

print("방문 순서 -- " , end = '')        
for i in visitedArray:
    print(i, end =' ')
    


