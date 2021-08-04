def d(n):    
    sum = 0
    sum += n
    while n > 0:        
        rest = n % 10 
        sum += rest
        n = n // 10
    return sum


arr = [i for i in range(1,10001)]
arr2 = []

for i in arr:
    result = d(i) # 만들어진 다음 수 
    arr2.append(result)
    
result = list(set(arr)-set(arr2))
result.sort()

for i in result:
    print(i)
    

