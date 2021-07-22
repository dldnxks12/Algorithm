'''

Quick Sort와 Selection Sort의 성능 비교

'''


# QuickSort function

def QuickSort(arr):

  n = len(arr)
  if n <= 1:
    return arr

  pivot = arr[n//2]
  rightArr = []
  midArr = []
  leftArr = []

  for i in arr:
    if i < pivot:
      leftArr.append(i)
    elif i == pivot:
      midArr.append(i)
    else:
      rightArr.append(i)
  
    return QuickSort(leftArr) + [pivot] + QuickSort(rightArr)


# Selection Sort  
# Method 1. 가장 작은 수 하나를 뽑아서 list에 추가 
# Method 2. 가장 작은 수 찾아서 자리 바꾸기 

def SelectionSort(arr):
  
  for i in range(len(arr)):
    for k in range(i, len(arr)):
      if arr[k] > arr[i]:
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp
 
  return arr

import random 
import time


# Data 1000 -> 3000 -> 5000 

Data1000 = [random.randint(1,10000) for i in range(1000)]
Data3000 = [random.randint(1,10000) for i in range(3000)]
Data5000 = [random.randint(1,10000) for i in range(5000)]

start1 = time.time()
QuickSort(Data1000)
end1 = time.time()
length1 = end1 - start1

start2 = time.time()
SelectionSort(Data1000)
end2 = time.time()

length2 = end2 - start2

print("QuickSort: ", length1 )
print("SelectionSort: ", length2 )

start1 = time.time()
QuickSort(Data5000)
end1 = time.time()
length1 = end1 - start1

start2 = time.time()
SelectionSort(Data5000)
end2 = time.time()

length2 = end2 - start2

print("QuickSort: ", length1 )
print("SelectionSort: ", length2 )

'''
QuickSort:  5.221366882324219e-05
SelectionSort:  0.08668160438537598
QuickSort:  6.365776062011719e-05
SelectionSort:  2.029723644256592
'''
