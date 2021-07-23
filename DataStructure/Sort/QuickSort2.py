'''

* Quick Sort : O( nlog(n) )

QuickSort1 에서는 왼쪽 그룹과 오른쪽 그룹을 위한 별도의 배열을 생성해서 사용하였다.

QuickSort2 에서는 원래 배열을 그대로 이용해본다

    - 재귀로 호출될 때마다  Start와 End를 전달받는다.
    - 만일 Start가 End보다 크거나 같다면 재귀를 종료한다. 즉, 정렬할 데이터가 1개 이하인 것 

'''


def QuickSort2(arr, start, end):

    if start >= end:
        return 
    
    low = start
    high = end
    pivot = arr[(low+high)//2] 

    while low <= high:
        while arr[low] < pivot:
            low+=1
        while arr[high] > pivot:
            high-=1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low+=1
            high-=1

    mid = low

    QuickSort2(arr, start, mid-1)
    QuickSort2(arr, mid, end)


def QSort(arr):
    QuickSort2(arr, 0, len(arr)-1)

dataArr = [188,162,168,120,100,170,50,150,50,200,105]

QSort(dataArr)

print(dataArr)



        

