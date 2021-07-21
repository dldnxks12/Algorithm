'''
Mean   : 전체 데이터를 모두 합한 후 데이터 수로 나누는 것
Median : 전체 데이터의 중앙값

'''
def SelectionSort(arr):
    
    temp = 0
    for i in range(len(arr)):
        for k in range(i , len(arr)):
            if arr[i] > arr[k]:
                temp = arr[i]
                arr[i] = arr[k]
                arr[k] = temp                
    return arr
        
DataArr = [7,5,11,6,9,80000,10,15,12]
print(SelectionSort(DataArr))
print("Median : {}".format(DataArr[len(DataArr)//2]))


