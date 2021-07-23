'''
 BFS(넓이 우선 검색) : 비선형 구조의 데이터 검색
    - Graph 완전 탐색 방법 
        - 횡방향으로 탐색 

    - 두 노드 사이의 최단 경로 또는 임의의 경로를 찾고 싶을 떄 사용 

    - Queue를 사용하여 구현 

        - 탐색할 노드의 순서를 저장하고 큐에 저장된 순서대로 탐색 

    1. root node에서 시작
    2. root node와 인접하며 방문하지 않았고, 큐에 저장되지 않는 Node를 Queue에 넣는다.
    3. Queue에서 Dequeue하여 가장 먼저 Queue에 저장된 노드를 방문한다.
'''

def enQueue(data):
    global Queue, front, rear, size

    if front == (rear+1) % (size):
        return 
    else:
        rear = (rear+1)%size
        Queue[rear] = data
        return 

def deQueue():
    global Queue, front, rear, size

    if front == rear:
        return 
    else:
        front = (front+1) % size
        data = Queue[front]
        Queue[front] = 0
        return data

front, rear = 0 , 0 
size = 10
Queue = [ 0 for _ in range(size)]

class Graph():
    def __init__(self,size):
        self.size = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]

def GraphViewer(G):
    print("Graph Viewer")        
    for row in range(G.size):
        for col in range(G.size):
            print(G.graph[row][col], end = ' ')
        print('')


def BFS(G):
    global Queue, front, rear, size
    current = 0 # Root node

    visitedVertex = []
    visitedVertex.append(current)
    
    while front != rear:
        for vertex in range(G.size):
            if G.graph[current][vertex] != 0: # If Connected
                if vertex in Queue:
                    continue
                else:
                    enQueue(vertex)
        for _ in Queue: # Queue에 있는 Vertex들을 대상으로 방문 실행        
            current = deQueue() # vertex 
            if current == 0 :
                continue
            visitedVertex.append(current)
            for vertex in range(G.size):
                if G.graph[current][vertex] != 0: # 해당 Vertex와 연결된 Vertex 라면 
                    if vertex in Queue or vertex in visitedVertex: # 해당 Vertex가 이미 Queue에 들어있다면 
                        continue
                    else:
                        enQueue(vertex) # 들어있지 않다면 Queue에 삽입               
        
    return visitedVertex
    

G = Graph(10)

G.graph[0][1] = 1;G.graph[0][2] = 1
G.graph[1][0] = 1;G.graph[1][3] = 1
G.graph[2][0] = 1;G.graph[2][3] = 1
G.graph[3][1] = 1;G.graph[3][2] = 1;G.graph[3][4] = 1
G.graph[4][3] = 1

GraphViewer(G)

print(BFS(G))


'''
Graph Viewer

0 1 1 0 0 0 0 0 0 0
1 0 0 1 0 0 0 0 0 0
1 0 0 1 0 0 0 0 0 0
0 1 1 0 1 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
[0, 1, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 2, 3, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 4, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

[0, 1, 2, 3, 4] -> 방문 노드 

'''