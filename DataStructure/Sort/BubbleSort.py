'''
* Bubble Sort : O(n^2)
    - 하지만 초기에 어느 정도 정렬이 되어 있다면 연산 수가 확연히 줄어드는 장점이 있다.

첫 번째 값부터 시작해서 바로 앞 뒤 데이터를 비교해서 큰 것은 뒤로 보내는 방법을 사용하는 정렬

'''

# Example of Bubble Sort


def BubbleSort(arr):

    for i in range(len(arr)-1,0,-1):
        for k in range(0,i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1] ,arr[k] 
    return arr

def BubbleSort2(arr): # 연산 수 감소시키는 법 -> 정렬이 일어나지 않는다면 바로 Quit
    for i in range(len(arr)-1,0,-1):
        ChangeYN = False
        for k in range(0,i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1] , arr[k] 
                ChangeYN = True
        if ChangeYN == False:
            break
    return arr

dataArr = [188,162,168,120,50,150,200,105]

print(BubbleSort(dataArr))
