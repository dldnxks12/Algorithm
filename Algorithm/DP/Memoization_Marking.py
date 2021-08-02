'''

황금 미로에서 부자되기

-- 지나온 길 Marking하기 

'''

def printarr(arr):
    
    for row in range(len(arr)):
        for col in range(len(arr)):
            print(arr[row][col], end = ' ')
        print('')

def MakeMemo(maze, memoization):            
    # 첫 행
    next = 0
    for i in range(5):
        next += maze[0][i]
        memoization[0][i] = next

    # 첫 열
    next = 0
    for i in range(5):
        next += maze[i][0]
        memoization[i][0] = next   

    # 두 번째 행에 대해서 최대값 갱신 
    for k in range(1,5):
        for i in range(1,5):
            memoization[k][i] = maze[k][i] + max(memoization[k-1][i], memoization[k][i-1])

def MakeMarking(memoization):
    start = 1
    for i in range(1,5):
        for k in range(start,5): 
            if memoization[i][k-1] > memoization[i-1][k]:
                memoization[i][k-1] = 0
                start = k
                break
            else:
                memoization[i-1][k] = 0

    memoization[0][0] = 0 # start
    memoization[4][4] = 0 # end 
    printarr(memoization)

maze = [
    [1,4,4,2,2],
    [1,3,3,0,5],
    [1,2,4,3,0],
    [3,3,0,4,2],
    [1,3,4,5,3]
                ]

memoization = [ [0 for _ in range(5)] for _ in range(5)]    

MakeMemo(maze, memoization)
MakeMarking(memoization)

