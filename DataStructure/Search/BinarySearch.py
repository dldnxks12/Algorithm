'''

Binary Search : O( log_2 N )

전체를 반쪽으로 나눠서 한 쪽씩 버리는 방식 : 순차 검색에 비해 성능이 월등히 좋다. (In Case of 정렬된 배열)

  - Divide and Conquer (분할 정복)

'''

def BinarySearch(arr, data):

  n = len(arr)
  start = 0
  end = n-1

  middle = n//2

  Find = False

  while True:
    print(arr[middle])
    if arr[middle] == data:
      Find = True
      break

    elif data < arr[middle]:
      end = middle-1
      middle = (start+end)//2

    else:
      start = middle+1
      middle = (start+end)//2

    if start >= end:
      Find = False
      break

  return Find

import random

arr = [ random.randint(1,100000) for _ in range(10000)]
arr.sort()

print(BinarySearch(arr, Data))

