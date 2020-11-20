## Fibonacci numbers using Bottom up DP

def Fib(n):
    fib = [0]*10000
    fib[0] = 1
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1]+fib[i-2]
    
    return fib[n]

if __name__ == "__main__":
    print(Fib(250))