'''
# 연락망에 없는 친구 찾기 

1. Graph들이 모두 이어져있는지 확인  
    - Vertex의 연결망 확인 
    - DFS로 모두 방문 후 VisitedArray에 누락된 Vertex 있는지 Check
2. Graph 종류 중 신장 트리 및 최소 비용 신장 트리 사용 


'''
# Graph Class 정의
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

def FindVertex(G, findvertex):

    stack = []
    visitedArray = []
    current = 0

    stack.append(current)
    visitedArray.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(size):
            if G.graph[current][vertex] == 1:
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


    print("방문 순서 -- ", end = '')
    for i in visitedArray:
        print(i, end = ' ') 

    if findvertex in visitedArray:
        print("연락 OK")
    else:
        print("연락 No")

    
size = 6
G = Graph(6)
# 문별 0, 솔라 1, 휘인 2, 쯔위 3, 선미 4 ,화사 5
G.graph[0][1] = 1;G.graph[0][2] = 1
G.graph[1][0] = 1;G.graph[1][3] = 1
G.graph[2][0] = 1;G.graph[2][3] = 1
G.graph[3][1] = 1;G.graph[3][2] = 1;G.graph[3][4] = 1
G.graph[4][3] = 1

FindVertex(G, 1)
 





    

