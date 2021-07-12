# 선형 리스트 

katok = []

def add_list(ss):
  katok.append(None)
  length = len(katok)
  katok[length-1] = ss

add_list("정현")
add_list("다현")
add_list("쯔위")
add_list("사나")
add_list("모모")


def Insertion(person, index):

  katok.append(None)

  for i in range(len(katok)-1, index, -1):
    katok[i] = katok[i-1]
    katok[i-1] = None
 
  katok[index] = person


def delate(index):

  katok[index] = None

  for i in range(index, len(katok)):
    if( i < len(katok)-1):
      katok[i] = katok[i+1]  
    else:
      break
  del(katok[len(katok)-1])  


