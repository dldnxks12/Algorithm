'''

2D Array 에서 중앙값 찾기 
    - 1D Array로 만든 후 중앙값 찾기 

'''


def SelectionSort(arr):

    for i in range(len(arr)):
        for k in range(i,len(arr)):
            if arr[i] > arr[k]:
                temp = arr[i]
                arr[i] = arr[k]
                arr[k] = temp
    
    return arr

array2D = [[55,22,250,33],
            [88,1,67,23],
            [199,222,38,47],
            [155,145,20,99]]

array1D = []

for i in array2D:
    for k in i:
        array1D.append(k)

print(array1D)
print(SelectionSort(array1D))

