'''

* Quick Sort : O( nlog(n) )

기준을 하나 뽑은 후 기준보다 작은 그룹과 큰 그룹을 나누어 다시 각 그룹으로 정렬하는 방법
각 그룹을 정렬하고자 재귀 호출을 하고, 각 그룹의 정렬이 완료되면 합치는 방식을 사용 

1. 기준 선정 -> 보통 가운데 값으로 선택 
2. 기준보다 작은 값들은 왼쪽 그룹, 큰 값들은 오른쪽 그룹으로 묶는다.
3. 각 그룹의 데이터 수가 1개가 되면 정렬 완료 

'''

def QuickSort(arr):

    n = len(arr)
    if n <= 1: # 정렬할 데이터 개수가 1개 이하면 종료
        return arr

    pivot = arr[n//2]
    leftArr  = [] 
    midArr   = []
    rightArr = []

    for i in arr:
        if i < pivot:
            leftArr.append(i)
        elif i == pivot:
            midArr.append(i)
        else:
            rightArr.append(i)
    
    return QuickSort(leftArr) + midArr + QuickSort(rightArr)
   
dataArr = [188,162,168,120,100,170,50,150,50,200,105]

print(QuickSort(dataArr))


