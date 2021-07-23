'''

# Heap

heap을 사용하는 가장 큰 이유는 최대, 최소값을 찾기 위함.

최소값, 최대값을 빠르게 찾아내는 자료구조 
   - 완전 이진 트리 구조

** Binary Search Tree와 헷갈릴 수 있지만, Head은 BST와 달리 최대, 최소 값만 Root node에 위치할 뿐 Child node에는 왼쪽 오른쪽을 나누는 규칙이 없다.

# 최소 힙 (최대 힙과 구현 방법은 동일)

Heap의 삽입 
1. 왼쪽 부터 오른쪽 순으로 leaf node에 추가 
2. 부모 노드와 비교 -> 부모 노드가 더 작다면 자리 교체

Heap의 삭제
1. root node를 삭제
2. leaf node에서 가장 오른쪽에 있는 node를 root node로 가져온 후 child node와 비교하며 더 작은 node가 있다면 자리 교체    

heap은 python에서 heapq module로 구현되있다.

# Priority Queue
일반적으로 Queue 는 FIFO 구조기 때문에 먼저 들어온 놈이 먼저 나간다.
But Priority Queue는 Heap을 사용하고,  내부적으로 정렬이 일어나기 때문에 데이터 내에서 우선순위가 높은 놈이 먼저 나간다.

'''

import heapq

# 데이터 추가 : heapq.heappush
result = []
heapq.heappush(result, 14)
heapq.heappush(result, 7)
heapq.heappush(result, 89)
heapq.heappush(result, 64)
print(result)
heapq.heappush(result, 1)
print(result)

# 데이터 삭제 heapq.heappop
heapq.heappop(result)  # root node만 제거
print(result)

# 기존 배열을 heap 구조로 변환 : heapq.heapify
arr = [3,2,6,4,1,10,509,28,0]
heapq.heapify(arr)
print(arr)


