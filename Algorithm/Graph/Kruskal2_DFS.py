
'''

가장 효율적인 방법으로 해저 케이블 망을 구축

    - 최소 비용 신장 트리 생성

'''

class Graph():
    def __init__(self,size):
        self.size = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]

def GraphViewer(G):
    print("--Graph--")
    for row in range(G.size):
        for col in range(G.size):
            print(G.graph[row][col],end=' ')
        print()         

def DFS(G, FindVertex):

    stack =[]
    visitedVertex = []
    current = 0
    
    stack.append(current)
    visitedVertex.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(G.size):
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
        else:
            current = stack.pop()

    if FindVertex in visitedVertex:
        return True
    else:
        return False


size = 6                
G = Graph(6)
# 서울 0 , 뉴욕 1, 북경 2, 방콕 3, 런던4, 파리 5
G.graph[0][1] = 80; G.graph[0][2] = 10
G.graph[1][0] = 80; G.graph[1][2] = 40; G.graph[1][3] = 70
G.graph[2][0] = 10; G.graph[2][1] = 40; G.graph[2][3] = 50
G.graph[3][1] = 70; G.graph[3][2] = 50; G.graph[3][4] = 30; G.graph[3][5] = 20
G.graph[4][3] = 30; G.graph[4][5] = 60; 
G.graph[5][3] = 20; G.graph[5][4] = 60; 

GraphViewer(G)

# 최소 비용 신장 트리 생성

# 1-1 Weight, Start, End list 생성
EdgeArray = []
for row in range(size):
    for col in range(size):
        if G.graph[row][col] != 0:
            EdgeArray.append([G.graph[row][col], row, col])

# 1-2 정렬

from operator import itemgetter

EdgeArray = sorted(EdgeArray, key = itemgetter(0), reverse=True)

NewArray = []

for i in range(0,len(EdgeArray), 2):
    NewArray.append(EdgeArray[i])

print(NewArray) # 내림차순으로 정렬

index = 0
while len(NewArray)-1 > size-1:

    Start = NewArray[index][1]
    End   = NewArray[index][2]
    SaveWeight = NewArray[index][0]

    G.graph[Start][End] = 0
    G.graph[End][Start] = 0

    if DFS(G,Start) and DFS(G,End): # 둘 다 Graph 상에 존재 
        del NewArray[index]
    else:
        G.graph[Start][End] = SaveWeight
        G.graph[End][Start] = SaveWeight
        index += 1

GraphViewer(G)

'''
--Graph--
0 0 10 0 0 0 
0 0 40 0 0 0 
10 40 0 50 0 0 
0 0 50 0 30 20 
0 0 0 30 0 60 
0 0 0 20 60 0 

'''
