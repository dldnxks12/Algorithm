'''

1. 콜센터는 9시에 영업시작
2. 9시 전부터 전화 문의 대기 
3. 고장 수리 3분 , 사용 문의 9분, 환불 문의 4분 , 기타 문의 1분 

  9시 이전에 고객이 전화를 하면 9시에 업무를 개시한 후 자신이 어느 정도 대기해야 하는지 시간을 알려준다.

'''

import numpy as np

def IsFull():
  global size, Queue, front, rear 

  if front == (rear+1)%size:
    return True
  else:
    return False

def IsEmpty():
  global size, Queue, front, rear 

  if front == rear:
    return True
  else:
    return False


def enQueue(data):
  global size, Queue, front, rear 

  if IsFull():
    return
  else:
    rear = (rear+1)%size
    Queue[rear] = data

def deQueue():
  global size, Queue, front, rear 

  if IsEmpty():
    return 
  else:
    front = (front+1)%size
    data = Queue[front]
    Queue[front] = None
    return data 

size  = 100
Queue = [None for _ in range(size)]  
front = 0 
rear  = 0 


if __name__ == "__main__":

  # data ->Type + 시간 인 tuple로 구성
  # deQueue 연산으로 data 하나씩 빼내어 시간 계산 

  enQueue(("사용", 9))
  enQueue(("환블", 4))
  enQueue(("기타", 1))
  enQueue(("사용", 9))
  enQueue(("환블", 4))
  enQueue(("기타", 1))
  enQueue(("사용", 9))

  
  Total_time = 0
  Waiting_time = [number[1] for number in Queue if number != None]

  print(Waiting_time)

  Total_time = np.sum(Waiting_time)

  print(Total_time, "분")
