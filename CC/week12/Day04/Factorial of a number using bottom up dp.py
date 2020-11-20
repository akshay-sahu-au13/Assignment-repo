## Factorial of a number using Bottom up DP:

# import time
# start_time = time.time_ns()
def fact(n):

    fact = [-1]*10005

    fact[0] = 1

    for i in range(1,n+1):
        fact[i] = fact[i-1]*i
    
    return fact[n]

if __name__ == "__main__":
    print(fact(100))
    # print(time.time_ns() - start_time, "nano-seconds")


    
