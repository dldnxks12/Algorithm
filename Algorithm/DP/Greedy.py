'''

가장 큰 이익의 데이터를 맨 먼저 선택하고, 그 다음 이익이 큰 데이터를 취하는 방식으로 데이터를 선택
    - 이 알고리즘을 사용하면 가장 효과적인 결과를 얻을 수 있지만, 그렇지 않는 경우도 존재한다.

    - 장점 : 적은 연산량
    - 단점 : 항상 최선의 결과를 보장하지는 않는다



# Basic Greedy Algorithm 문제

    거스름 돈 
    1. 500원, 100원, 50원 , 10원 짜리 동전히 무한히 존재
    2. 손님에게 거슬러 줘야 할 돈이 N원일 때, 거슬러 줘야할 동전의 최소 개수 
    3. 단, 거슬러 줘야할 돈 N은 항상 10의 배수 

'''

def coins(money):
    global coin

    data = money
    count = 0 
    while data >= 500:        
        data = data - 500
        print(data)
        count += 1 

    while data >= 100:
        data = data - 100
        print(data)
        count +=1

    while data >=50:
        data = data - 50
        print(data)
        count +=1
    while data >=10:
        data = data -10
        print(data)
        count +=1
    
    return count

coin = [500,100,50,10]

print(coins(1330))