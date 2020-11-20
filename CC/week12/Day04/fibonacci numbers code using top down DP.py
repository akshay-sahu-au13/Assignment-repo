## Calculating Fibonacci numbers using Top down DP

Dp = [-1]*10000

def Fib(n):
    if n == 0 or n == 1:
        return 1
    if Dp[n] != -1:
        return Dp[n]
    
    Ans = Fib(n-1) + Fib(n-2)
    Dp[n] = Ans

    return Ans

if __name__ == "__main__":
    print(Fib(100))