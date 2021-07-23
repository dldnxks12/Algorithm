'''


 # Brute Force
 # Backjoon 1065 한수 
 
    어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면 한수이다.

    임의의 수 N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램 

    -> Sequential Search 를 통한 Brute Force로 해결 
        
        선형 데이터이기 떄문에 BFS가 아닌 Sequential Search 사용

'''

def Hansu(data): # N은 숫자 길이 if N = 1000
    
    # 1. 자리수 구하기  // : 몫, / 목+소수점 , % 나머지
    
    length = 0

    N = data
    while N != 0:
        N = N//10
        length += 1

    # if 122 일 때 -> length : 3
    # 각 자리수 도출

    arr = []
    while length != 0:
        print(length)
        length -= 1
        minus = data // pow(10,length)
        arr.append(minus)
        minus *= pow(10,length)
        data = data-minus

    arr2 = []
    for i in range(len(arr)):
        if i != 0:
            diff = arr[i] - arr[i-1]
            arr2.append(diff)

    for i in range(len(arr2)):
        if i != 0:
            if arr2[i] == arr2[i-1]:
                continue
            else:
                return False

    return True

# Find Hansu

count = 0 
for i in range(N+1):
    if i != 0:
        if Hansu(i):
            count +=1

print(count)




    
    



