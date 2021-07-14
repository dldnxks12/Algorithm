'''

front , rear 초기값 0 

  --> front == rear -> Queue is Empty
  
    --> Circular Queue는 전체에서 한 칸 적게 사용 (front == rear인 경우 Queue가 꽉찬 경우에도 해당되지만 이는 제외)
 
  --> front == (rear+1)%(size) -> Queue is Full

'''


def IsQueueFull():
  global front, rear, size, Queue

  if front == (rear+1)%size :
    return True
  else:
    return False

def IsQueueEmpty():
  global front, rear, size, Queue

  if front == rear  :
    return True
  else:
    return False
  

def enQueue(data):
  global front, rear, size, Queue  
  if IsQueueFull():
    return
  else:
    rear = (rear+1)%size
    Queue[rear] = data
    
def deQueue():
  global front, rear, size, Queue  
  if IsQueueEmpty():
    return 
  else:
    front = (front+1)%size
    data = Queue[front]
    Queue[front] = None
    return data 

size  = 10
Queue = [ None for _ in range(size)]
front = 0
rear  = 0


if __name__ == "__main__":

  enQueue("종수1")
  enQueue("종수2")
  enQueue("종수3")
  enQueue("종수4")
  enQueue("종수5")
  enQueue("종수6")
  enQueue("종수7")
  enQueue("종수8")
  enQueue("종수9")
  data = deQueue()
  data = deQueue()
  enQueue("종수10")
  enQueue("종수11")
  data = deQueue()
  data = deQueue()
  data = deQueue()
  data = deQueue()  

  print(Queue)
