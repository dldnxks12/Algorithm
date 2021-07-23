'''

    # 최단 경로 알고리즘 
    - Robot Navigation에도 자주 사용되는 알고리즘 (A* Algorithm와 비슷)
    - 하나의 시작 Node에서 나머지 모든 Node로의 최단 경로를 찾는다.
    
    # 사용 개념 - Queue 개념 없이 구현 
    1. Weighted Graph
    2. BFS
    3. Greedy Algorithm

    # Queue or Heap을 이용한 Dijkstra 구현도 추후 해볼 것 

'''

class Graph():
    def __init__(self,size):
        self.size = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size) ]
        

def GraphViewer(G):
    print("Graph Viewer")

    for row in range(G.size):
        for col in range(G.size):
            print(G.graph[row][col], end = '   ')
        print()        


# BFS를 이용해서 Dijkstra Algorithm 설계 
# 1. 시작 노드와 인접하지 않는 노드 모두 inf로 설정
# 2. 현재 노드에서 가장 작은 값을 갖는 노드 선택
# 3. 해당 노드 VisitedQueue에 넣기
# 4. 해당 노드와 인접한 노드들로의 가중치 값과 이전 노드에서 저장해둔 값 중 작은 값으로 Update
#       -> D(v) = D(v) or D(w) + C(w,v)
# 5. visitedQueue에 없는 다음 노드 선택 

inf = float("inf") # 무한대 설정

def dijkstar(G):
    start = 0
    visitedQueue = []
    visitedQueue.append(start)

    # initialize
    for row in range(G.size):
        for col in range(G.size):
            if G.graph[row][col] == 0:
                G.graph[row][col] = inf
    GraphViewer(G)

    # Vertex 0 : inf   10   15   inf   inf   inf  : 0번 Vertext to 1번 Vertex 10 , 0번 Vertex to 4번 Vertex inf...

    while len(visitedQueue) != G.size:
        data = min(G.graph[start])
        idx = G.graph[start].index(data) # 최소값을 갖는 vertex         
        if idx in visitedQueue:
            TempQueue = G.graph[start][:] # Shallow Copy
            while True:
                TempQueue.remove(data)  # 해당 Index에 해당하는 최소값 삭제
                data = min(TempQueue)
                idx = G.graph[start].index(data) # 최소값을 갖는 vertex 
                if idx in visitedQueue:
                    continue
                else:
                    break            
        print(idx)                
        visitedQueue.append(idx) # 방문한 Node에 추가 
        # 비교 -  G.graph[current][idx] + G.graph[idx][3] 과 G.graph[current][3]
        for vertex in range(G.size):
            if start == vertex: # 자기 자신으로는 안 갈 것 
                continue
            if G.graph[start][vertex] > G.graph[start][idx] + G.graph[idx][vertex]: # 바로 가는 것보다, 지금 선택한 노드를 통해서 가는 것이 더 효율적이라면? 
                G.graph[start][vertex] = G.graph[start][idx] + G.graph[idx][vertex] # 값 보정 
            
    print(visitedQueue) # [0, 1, 2, 3, 4, 5]
    print(G.graph[start]) # [inf, 10, 15, 21, 41, 51]

# Graph

size = 6
G = Graph(6) 
G.graph[0][1] = 10; G.graph[0][2] = 15
G.graph[1][0] = 10; G.graph[1][2] = 40; G.graph[1][3] = 11; G.graph[1][4] = 50
G.graph[2][0] = 15; G.graph[2][1] = 40; G.graph[2][3] = 12
G.graph[3][1] = 11; G.graph[3][2] = 12; G.graph[3][4] = 20; G.graph[3][5] = 30
G.graph[4][1] = 50; G.graph[4][3] = 20; G.graph[4][5] = 25
G.graph[5][3] = 30; G.graph[5][4] = 25

# Queue 
front, rear = 0 , 0 
Queue = [0 for _ in range(size)] 

dijkstar(G)




