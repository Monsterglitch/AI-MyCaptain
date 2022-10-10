def FibRecursion(n):  
    if n <= 1:  
       return n  
    else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  
 
print("Fibonacci sequence for first 15 terms:")  
for i in range(15):  
    print(FibRecursion(i), end=" ")
