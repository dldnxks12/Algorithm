'''

판매된 물건 목록과 개수 세기

# 사용 알고리즘 

1. 정렬 : Quick Sort
2. 검색 : Binary Search 

'''
import random

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

def BinarySaerch(arr, data):

    n = len(arr)
    start = 0
    end = n-1    
    mid = n//2

    while start <= end:      
      if arr[mid] == data:
        return True
      elif data < arr[mid]:
        end = mid - 1
        mid = (start+end)//2
      else:
        start = mid + 1 
        mid = (start+end)//2
    return False

dataArr = ['바나나', '레쓰비', '츄파츕스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sellArr = [ random.choice(dataArr) for _ in range(100)]
# 1. Array 정렬
SortedsellArr = QuickSort(sellArr)
# 2. 판매물건 Search and make list

Todaylist = []

for i in SortedsellArr:
  count = 0
  if BinarySaerch(SortedsellArr,i): # In list 
    for k in range(len(sellArr)):
      if sellArr[k] == i:
        count += 1
    Todaylist.append([i,count])

print(Todaylist)  
