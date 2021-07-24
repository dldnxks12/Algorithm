'''

# Memoization

    주어진 입력값에 대한 결과를 저장함으로써 같은 입력값에 대해 함수가 한 번만 실행되도록 한다.
    
    재귀함수를 사용하는 경우에 함수 Call이 과도하게 일어날 경우 과도하게 Stack 메모리를 사용할 수도 있고,
    심지어 탈출 조건을 제대로 설정하지 않는다면 Stack overflow가 일어날 수 있다.

    이러한 경우를 대비하여 반복되는 특정 단계의 재귀함수 결과값을 저장하여 사용하는 방법인 Memoization을 잘 사용할 수 있어야한다.


C 또는 C++을 사용할 시 memset과 배열을 사용하여 다음과 같이 구현한다. 피보나치를 예로 이해해본다.

# 피보나치 수열의 정의

Fn  = 0 if n == 0
    = 1 if n == 1
    = Fn-1 + Fn-2 if n > 1

1. Memorization을 사용하지 않은 피보나치 수열

int fibo(int n)
{
    if n == 0
        return 0
    elif n == 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
}

2. memoization을 사용한 피보나치 수열 

int fibo(int n)
{
    if n == 0
        return 0
    elif n == 1
        return 1
    if dp[n] != -1  # 해당하는 수가 이미 저장되어 있다면 ??? 요거 바로 쓰자 !
        return dp[n]
    
    return fibo(n-1) + fibo(n-2)
}

int dp[50];

int main(void)
{
    memset(dp, -1, sizeof(dp)); # dp 배열을 모두 -1로 초기화
}

'''

# Python에서의 Memoization 

dp = [-1 for _ in range(50)] # 크기 50인 배열 -1로 초기화

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1: # Memoization : 결과값 저장해두었다 사용 
        return dp[n]
    else:
        return fibo(n-1) + fibo(n-2)        

print(fibo(7))

