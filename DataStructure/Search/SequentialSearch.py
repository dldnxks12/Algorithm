'''

Sequential Search : O(n)

정렬되지 않은 데이터의 순차 검색 
  - 맨 앞부터 차례로 검색

'''

def SequentialSearch(arr, data):

  Idx = -1

  for i in range(len(arr)):
    if arr[i] == data:
      Idx = i
      break

  if Idx == -1:
    return False
  else:
    return True


'''

O(n)

정렬된 데이터의 순차 검색
  - 검색하는 방법은 동일하나 데이터가 해당 배열에 없는 경우에 검색을 중단할 수 있다.
    - If 찾는 데이터의 크기가 해당 범위 내에 없다면 그 즉시 검색을 중단한다.

'''

def SequentialSearch2(arr,data):
  
  idx = -1
  for i in range(len(arr)):
    if arr[i] == data:
      idx = i
    if data < arr[i]:
      break
  if idx == -1:
    return False
  else:
    return True


arr = [1,2,3,4,5,10]  

print(SequentialSearch2(arr,1))
  
        

