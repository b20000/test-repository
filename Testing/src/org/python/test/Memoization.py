class Memoization(object):
    
    def fib(self,n):
        a,b = 1,1
        for n in range(n-1):
            a,b = b, a+b 
        
        return a

    def memoize(self,fn,arg):
        
        memo = {}
        if arg not in memo:
            memo[arg] = fn(arg)
        
        return memo[arg]
    
if __name__ == '__main__':
    
    obj = Memoization()
    
    i=0
    while i < 5:
        print obj.fib(i)
        i = i+1
    #print obj.memoize(obj.fib, 5)