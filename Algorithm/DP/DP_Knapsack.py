'''

무게와 가격이 다른 여러 물건 중에서 가장 효율적으로 배낭에 채우기 위한 문제.

보석은 총 4개 
배낭에 담을 수 있는 무게 총 7kg

1. 2차원 배열 구성
    행 : 물건의 최대개수 0 ~ 4
    열 : 배낭에 담을 수 있는 무게 0 ~ 7  

'''


# 2차원 배열 구성

def knapsack():

    global MaxWeight, RowCount, weight, money

    array = [ [0 for _ in range(MaxWeight+1)] for _ in range(RowCount+1) ] #5행 8열

    for k in range(RowCount):
        for i in range(MaxWeight+1):
            if i < weight[k+1]:
                array[k+1][i] = array[k][i]
            else:
                array[k+1][i] = max( money[k+1] + array[k][i-weight[k+1]], array[k][i] )
    print(array)

MaxWeight = 7
RowCount = 4

weight = [0,6,4,3,5]   # 보석 무게
money  = [0,13,8,6,12] # 보석 가격 

knapsack()