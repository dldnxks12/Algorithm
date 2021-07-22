'''
# Color Image 3 channel 2 Dimensional Image 
# Gray Scale Image 3 Channel 2 Dimensional Image
# Color to Gray Scale 을 위해 우선 Color Image를 1D Array로 만든 후 중앙값을 찾아야함

r,g,b = photo.get(i,k)  # i 행 k열 Pixel의 RGB Pixel Value
value = (r+g+b)//3 # mean value
photoArr.append(value)  # 1D Array로 만들기
'''

from tkinter import *

window = Tk()
window.geometry("600x600")

photo = PhotoImage(file = 'pet.gif')

photoArr = []  # 1D Array

for i in range(h):
  for k in range(w):
    r,g,b = photo.get(i,k)
    value = (r+g+b)//3
    photoArr.append(value)


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

   return QuickSort(leftArr) + [pivot] + QuickSort(RightArr) 

# photoArr의 중앙값으로 Threshold -> QuickSort를 이용해서 Median Value 찾기

photoArr = QuickSort(photoArr) # 정렬된 1D Array

MedianValue = photoArr[len(photoArr)//2]

for i in range(len(photoArr)):
  if photoArr[i] > MedianValue:
    photoArr[i] = 255
  else:
    photoArr[i] = 0 

# 다시 2D Array로 돌려보내주기
pos = 0 
for i in range(h):
  for k in range(w):
    r = g = b = photoArr[pos]
    pos += 1
    photo.put("#%02x%02x%02x" % (r,g,b),(i,k))


paper = Label(window, image=photo)  # Title 
paper.pack(expand=1, anchor = center)

window.mainloop()


