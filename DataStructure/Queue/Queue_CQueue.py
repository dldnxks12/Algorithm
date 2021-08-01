# Queue  1. enqueue, dequeue

def enQueue(data):

  global Queue, size, front, rear

  if rear == size-1:
    print("Queue is Full")
    return

  rear = rear + 1
  Queue[rear] = data
  return 

def deQueue():

  global Queue, size, front, rear

  if front == rear:
    print("Queue is Empty")
    return 

  front = front + 1
  data = Queue[front]
  Queue[front] = None
  return data

Queue = [None for _ in range(size)]
size = 100
front, rear = -1, -1 

# Circular Queue

def CenQueue(data):
  
  global Queue, size, front, rear
  
  if front == (rear + 1) % size :
    print("Queue is Full")
    return

  rear = (rear+1) % size
  Queue[rear] = data

  return 

def CdeQueue():

  global Queue, size, front, rear

  if front == rear:
    print("Queue is Empty")
    return 

  front = (front+1) % size 
  data = Queue[front]
  Queue[front] = None
  return data

Queue = [ None for _ in range(size)]
size = 100
front, rear = 0, 0 
