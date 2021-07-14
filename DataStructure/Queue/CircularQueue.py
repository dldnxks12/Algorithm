'''

front , rear 초기값 0 

  --> front == rear -> Queue is Empty
  
    --> Circular Queue는 전체에서 한 칸 적게 사용 (front == rear인 경우 Queue가 꽉찬 경우에도 해당되지만 이는 제외)
 
  --> front == (rear+1)%(size) -> Queue is Full

'''
