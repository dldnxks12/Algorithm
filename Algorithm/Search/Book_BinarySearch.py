'''

Binary Search

Index 이용한 도서관 책 찾기 

책 제목만 적어 가나다 순서로 정렬한 후 책 제목 옆에 실제로 책이 꽂혀 있는 위치를 기록해놓자.
  - 책 제목만 찾은 후 옆에 적힌 위치에서 책을 찾으면 된다. 

'''

from operator import itemgetter

def BinarySearch(arr, data):

  n = len(arr)
  start = 0
  end = n-1

  middle = n//2

  while True:
    if arr[middle][0] == data:
      return arr[middle][1]
    elif data < arr[middle][0]:
      end = middle -1
      middle = (start+end)//2
    else:
      start = middle+1
      middle = (start+end)//2
    
    if start >= end:
      return False


def makeIndex(arr,pos):

  beforeArr = []
  index = 0
  for data in arr:
    beforeArr.append((data[pos],index))
    index +=1

  sortedArr = sorted(beforeArr, key = itemgetter(0) )
  return sortedArr


BookArr = [  ['어린왕자','생텍쥐베리'],['이방인','까뮈'],['부활','톨스토이'],['신곡','단테'],['돈키호테','세르반데스'],['동물농자','조지오웰'],['데미안','헤르만헤세']  ]

nameIdx = []
authorIdx = []


nameIdx = makeIndex(BookArr,0)
authorIdx = makeIndex(BookArr,1)

print(nameIdx)
print(authorIdx)


print(BinarySearch(nameIdx, '어린왕자'))

