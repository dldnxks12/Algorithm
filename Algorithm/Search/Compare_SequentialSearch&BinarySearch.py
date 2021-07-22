'''
# 순차 검색과 이진 검색 성능 비교 알고리즘 구현

1. 데이터 100만 개를 랜덤하게 생성해서 정렬되지 않은 배열과 정렬된 배열을 각각 준비
2. 정렬되지 않은 데이터에서 순차 검색 사용 -> 몇 번만에 찾는지 
3. 정렬된 데이터에서 이진 검색 사용 -> 몇 번만에 찾는지 

'''


import random

def SequentialSearch(arr, data):

  Idx = -1
  count = 0
  for i in range(len(arr)):
    count += 1
    if data == arr[i]:
      Idx = i
      break
      return Idx

  if Idx == -1:
    return Idx, count
  else:
    return Idx, count

def BinarySearch(arr, data):

  n = len(arr)
  start = 0
  end = n-1
  mid = n//2
  count = 0

  while start <= end:
    count += 1
    if arr[mid] == data:
      return mid, count 
    elif data < arr[mid]:
      end = mid-1
      mid = (start+end)//2
    else:
      start = mid + 1
      mid = (start+end)//2

  return -1, count 

arr1 = [random.randint(1,10000000) for _ in range(1000000)]
arr2 = arr1
arr2.sort()

data = random.choice(arr1)

print(SequentialSearch(arr1,data))
print(BinarySearch(arr2,data))

'''
(250106, 250107) - 순차 검색 250107번
(250106, 20)     - 이진 검색 20번
'''
