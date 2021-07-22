'''

이미 배열이 Sorting된 상태에서 맨 마지막 값이 아무 위치에나 끼어들 때, 다시 정렬하는 효율적인 방법 -> Bubble Sort가 이 상황에서 좋은 성능을 보인다
Quick Sort는 어떨지 확인해보자

'''

import random
import time

def BubbleSort(arr):
  
  end = len(arr)
  for i in range(end-1, 0 , -1):
    ChangeTF = False
    for k in range(0,i):
      if arr[k] > arr[k+1]:
        arr[k], arr[k+1] = arr[k+1], arr[k]
        ChangeTF = True
    if ChangeTF == False:
      break

  return arr

def QuickSort(arr):
  
  n = len(arr)
  if n <= 1:
    return arr

  pivot = arr[n//2]
  leftArr = []
  midArr = []
  rightArr = []

  for i in arr:
    if i < pivot:
      leftArr.append(i)
    elif i == pivot:
      midArr.append(i)
    else:
      rightArr.append(i)

  return QuickSort(leftArr) + [pivot] + QuickSort(rightArr)


Arr = [ random.randint(1,10000) for _ in range(10000)]
Arr.sort()

Index = random.randint(1,9999)
Arr.insert(Index, Arr[len(Arr)-1])

start = time.time()
BubbleSort(Arr)
end = time.time()
length = end - start

Index = random.randint(1,9999)
Arr.insert(Index, Arr[len(Arr)-1])

start2 = time.time()
QuickSort(Arr)
end2 = time.time()
length2 = end2 - start2

print(length)
print(length2)

'''

Bubble : 0.002695798873901367
Quick  : 0.01809525489807129

이미 일정부분 정렬되 있는 배열에서는 Bubble Sort가 더 좋은 성능을 보인다.

'''
