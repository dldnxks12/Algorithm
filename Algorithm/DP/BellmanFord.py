'''

시작 정점 -> 다른 정점까지의 최단 경로 Algorithm

1. 음수 가중치가 있는 그래프의 최단 경로 찾을 수 있다.
2. 음수 사이클 존재의 여부를 알 수 있다.
    
        ** 음수 사이클 안에서 무한으로 뺑뺑이 도는 경우를 알 수 있는 방법
    
        그래프 정점의 개수를 V라고 할 떄, 인전 간선을 검사하고 거리 값을 갱신하는 과정을 V-1번으로 제한하면 가능
        그래프의 시작 정점에서 특정 정점까지 도달하기 위해 거쳐 가는최대 간선 수는 V-1개 이기 때문
            -> V번 째 간선이 추가되는 순간 무한 사이클에 빠진 것을 알 수 있음

'''

inf = float("inf")

class Graph():
    def __init__(self,size):
        self.size = size
        self.graph = [ [ inf for _ in range(size)] for _ in range(size)]

def GraphViewer(G):
    print("Graph Viewer")

    for row in range(G.size):
        for col in range(G.size):
            print(G.graph[row][col], end = '   ')
        print()        


def BellmanFord(G):
    for row in range(G.size):
        for col in range(G.size):
            if row == col:
                G.graph[row][col]=0 

    for _ in range(G.size-1):
        for current in range(G.size): # V = G.size
            for vertex in range(G.size):
                for idx in range(G.size):
                    if G.graph[current][idx] > G.graph[current][vertex] + G.graph[vertex][idx]: # 둘러가는 것이 더 효율적?
                        G.graph[current][idx] = G.graph[current][vertex] + G.graph[vertex][idx] # 값 보정

    GraphViewer(G)

    for current in range(G.size): # V = G.size
        for vertex in range(G.size):
            for idx in range(G.size):
                if G.graph[current][idx] > G.graph[current][vertex] + G.graph[vertex][idx]: # 둘러가는 것이 더 효율적?
                    return False

    GraphViewer(G)
    
    return True


size = 6

G = Graph(6) 
G.graph[0][1] = -10; G.graph[0][2] = 15
G.graph[1][0] = -10; G.graph[1][2] = 40; G.graph[1][3] = 11; G.graph[1][4] = 50
G.graph[2][0] = 15; G.graph[2][1] = 40; G.graph[2][3] = 12
G.graph[3][1] = 11; G.graph[3][2] = 12; G.graph[3][4] = 20; G.graph[3][5] = 30
G.graph[4][1] = 50; G.graph[4][3] = 20; G.graph[4][5] = 25
G.graph[5][3] = 30; G.graph[5][4] = 25

GraphViewer(G)

TF = BellmanFord(G)

print(TF)

'''

Graph Viewer
0   10   15   inf   inf   inf
10   0   40   11   50   inf
15   40   0   12   inf   inf
inf   11   12   0   20   30
inf   50   inf   20   0   25
inf   inf   inf   30   25   0

Graph Viewer
0   10   15   21   41   51
10   0   23   11   31   41
15   23   0   12   32   42
21   11   12   0   20   30
41   31   32   20   0   25
51   41   42   30   25   0

True

if 음수 데이터 in it 

'''