'''

* Insertion Sort : O(n^2)

* 기존 데이터 중에서 자기 자리를 찾아 들어가는 정렬


1. 데이터를 자기 보다 작은 데이터 뒤, 큰 데이터 앞에 삽입 
    - 데이터를 비교해가며 자기 보다 큰 놈이 등장하면 그 바로 앞에 들어가자.
2. 모든 데이터에 대해 반복 

'''

def InsertionSort(arr):

    SortedArr = []
    SortedArr.append(arr[0])

    for i in range(len(arr)): # Data Array
        for k in range(len(SortedArr)): # Backet Array
            if SortedArr[k] > arr[i]:
                if k == 0:
                    SortedArr.insert(0, arr[i])  
                    break  
                else:
                    SortedArr.insert(k, arr[i])
                    break
            if k == len(SortedArr)-1 and SortedArr[k] < arr[i]:
                SortedArr.append(arr[i])                    
    return SortedArr

arr = [10,30,20,60,40,70,100,80,90]

print(InsertionSort(arr))


def InsertionIndex(arr, data):

    Idx = -1
    for i in range(len(arr)):
        if arr[i] > data:
            Idx = i
            break        
    if Idx == -1:
        return len(arr)
    else:
        return Idx

