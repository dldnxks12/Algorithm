# Recursive Addition
def Add(num):

    if num <= 1:
        return 1
    else:        
        return num + Add(num-1)
    

#print(Add(10))

# 두 수를 입력받고 두 숫자 사이 합계를 구하는 코드 

def Add2(num, num2):

    if num <= num2:
        if num2 <= num:
            return num
        else:
            return num2 + Add2(num, num2-1)
    else:
        if num <= num2:
            return num2
        else:
            return num + Add2(num -1, num2)

#print(Add2(1, 3))

# Factorial
def factorial(num):

    if num <= 1:
        return num
    else:
        return num*factorial(num-1)

#print(factorial(3))

# CountDown
def CountDown(num):

    if num == 1:
        return print(num)
    else:
        print(num)
        num -=1    
        return CountDown(num)

# Star Shape : High -> low
def StarShape(number):

    if number > 0:
        StarShape(number-1)
        print("*"*number)

#StarShape(5)        

# Star Shape : High -> low            

def StartShapeLH(n,number):
    print(n)
    if n <= number:        
        StartShapeLH(n+1,number)
        print("*"*n)
        return         
# StartShapeLH(1,5)

# 구구단 1단 ~ 9단 
def KK(dan):
    if dan == 1 :        
        pass
    else:
        KK(dan-1)

    for i in range(9):
        print("{} x {} = {}".format(dan, i+1 ,(i+1)*dan))

# KK(9)

# 제곱수 
def pow(x, n): # x의 n승 
    if n > 1:        
        return x*pow(x, n-1)  # 2 * pow(2,3) -> 2*2*pow(2,2) -> 2*2*2*pow(2,1)
    else:
        return x

# 배열의 합 

def ArraySum(Array,num):
    if num < len(Array)-1:
        return Array[num] + ArraySum(Array , num+1)
    else:
        return Array[len(Array)-1]

Array = [150,71,135,53,16]

print(ArraySum(Array, 0))




    



