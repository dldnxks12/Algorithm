'''

FIFO 

1. EnQueue
2. DeQueue
3. Front / Rear  둘 다 -1 --> Queue Empty

'''

def IsQueueFull():
  
  if rear == size -1 :
    return True
  else:
    return False

def IsQueueEmpty():
  
  if front == rear:
    return True
  else:
    return False

def enQueue(data):
  
  if IsQueueFull():
    return 
  else:
    rear += 1
    Queue[rear] = data

def deQueue():
  
  if IsQueueEmpty():
    return 
  else:
    front += 1
    data = Queue[front]
    Queue[front] = None
    return data  

def peek():

  if IsQueueEmpty():
      return 
  else:
    return Queue[front+1]  

size = 100
Queue = [ None for _ in range(size)]
front = -1
rear  = -1

