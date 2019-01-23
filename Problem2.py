#Sum of Even Fibonacci Numbers Unitil the number Exceeds 4 million

#Recursive function to find Fibonacci of the number
def fib(n):
    if (n == 0 or n == 1):
        return(1)
    else:
        return(fib(n-1) + fib(n-2))

#Printing out Sum of even Fibonacci numbers
def testFib(n):
    sum = 0
    for i in range(1,n):
        #print(fib(i))
        if (fib(i) % 2 == 0):
            sum = sum + fib(i)
    print(sum)

#Not exceeding 4 million
testFib(33)
