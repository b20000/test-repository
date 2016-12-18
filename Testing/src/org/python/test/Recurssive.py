def fibonacci(n):
        
    if (n == 0):
        return n
    elif( n==1):
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

def factorial( n):
        
    if (n == 0):
        return n
    elif( n==1):
        return n
    else:
        return factorial(n-1)* n
    

for items in xrange(5):
    print fibonacci(items)
    
print factorial(5)