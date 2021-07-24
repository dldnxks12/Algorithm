'''

황금 미로에서 부자되기

    - 메모이제이션을 사용할 것 

    - 해당 예제는 재귀적인 방법을 사용하지 않아 사실상 메모이제이션의 성능을 크게 보여주지는 못하는 예제이다.
    - 하지만 메모이제이션의 기본 개념인 값을 저장한 후 단순히 반환받아 사용하는 것을 연습해본다.

'''

def printarr(arr):
    
    for row in range(len(arr)):
        for col in range(len(arr)):
            print(arr[row][col], end = ' ')
        print('')

maze = [
    [1,4,4,2,2],
    [1,3,3,0,5],
    [1,2,4,3,0],
    [3,3,0,4,2],
    [1,3,4,5,3]
                ]
memoization = [ [0 for _ in range(5)] for _ in range(5)]                

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

printarr(memoization)