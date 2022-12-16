def nth_fib(n):
    #Base Case
    if n <= 1:
        return n
    
    #Recursive Case
    else:
        return(nth_fib(n-1) + nth_fib(n-2))
