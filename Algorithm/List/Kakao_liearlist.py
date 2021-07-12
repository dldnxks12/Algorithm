# 카톡 친구 자동 삽입 with Linear List

katok = [ ('다현',200), ('정연',150),('쯔위',90), ('사나',30), ('지효',15)]

# 1. 삽입 함수 

def Insertion(index, data):
  katok.append(None)

  for i in range(len(katok)-1, index, -1):
    katok[i] = katok[i-1]
    katok[i-1] = None
  katok[index] = data

# 2. 삭제 함수

def delate(index):
  katok[index] = None

  for i in range(index, len(katok)-1):
    if (i < len(katok)):
      katok[i] = katok[i+1]
    else:
      break
  
  del(katok[len(katok)-1])

# 3. 숫자 비교 -> 알맞은 Index 찾기

name = input("이름 :")
num = int(input("카톡 횟수: "))
data = (name, num) # 비교에 넣을 Data

compare = [ i[1] for i in katok ] # 카톡 횟수

compare.append(num)
compare.sort()
compare.reverse()
Index = compare.index(num)

Insertion(Index, data)
print(katok)
