'''

* Selection Sort : O(n^2)

* 여러 데이터 중에서 가장 작은 값을 뽑는 작동을 반복해서 값을 정렬하는 방법 

* 최솟값 찾기
    1. 배열의 첫 원소를 최솟값으로 설정
    2. 다음 원소들과 하나씩 비교
    3. 끝까지 비교한 후 최솟값 걸러내고 다시 

'''

# ---- Type 1. Array 2개 사용 ---- #

def Min(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]

    return min

arr = [4,1,7,5,2,3,40,38]
SortedArr = []

for _ in range(len(arr)):
    MinData = Min(arr) # 하나씩 넣어보기
    SortedArr.append(MinData)
    arr.remove(MinData)  # 해당 값 제거 

print(SortedArr)

# ---- Type 2. Array 1개 사용 ---- #

arr2 = [4,1,7,5,2,3,40,38]

for i in range(len(arr2)):
    for k in range(i,len(arr2)): 
        if arr2[i] > arr2[k]:
            temp = arr2[i]
            arr2[i] = arr2[k]
            arr2[k] = temp            

print(arr2)






