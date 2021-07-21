'''
성적 순대로 삽입 정렬 후 짝 지어주기
'''

def InsertionSort(arr):
    SortedArr = []
    SortedArr.append(arr[0])

    for i in range(len(arr)):
        for k in range(len(SortedArr)):
            if SortedArr[k] > arr[i]:
                if k == 0:
                    SortedArr.insert(0, arr[i])
                else:
                    SortedArr.insert(k, arr[i])
            if k == len(SortedArr)-1 and arr[i] > SortedArr[k]:
                SortedArr.append(arr[i])

    return SortedArr

def InsertionSort2(arr):

    SortedArr = []
    SortedArr.append(arr[0])

    for i in range(len(arr)): # Data Array
        for k in range(len(SortedArr)): # Backet Array
            if SortedArr[k][1] > arr[i][1]:
                if k == 0:
                    SortedArr.insert(0, arr[i])    
                    break
                else:
                    SortedArr.insert(k, arr[i])
                    break
            if k == len(SortedArr)-1 and SortedArr[k][1] < arr[i][1]:
                print(arr[i])
                SortedArr.append(arr[i])                    
    return SortedArr

ScoreArr = [['선미',88], ['초아',99],['화사',71],['영탁',78],['영웅',67],['민호',92]]
SortedArr = InsertionSort2(ScoreArr)

print(SortedArr)
CoupleList = []

for i in range(0,len(ScoreArr)//2):
    CoupleList.append([SortedArr[i] , SortedArr[len(ScoreArr)-i-1]])

print(CoupleList)


