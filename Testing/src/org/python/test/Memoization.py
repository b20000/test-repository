
class Memoization(object):
    
    #@Memoize
    def fib(self,n):
        a,b = 1,1
        for n in range(n-1):
            a,b = b, a+b 
        
        return a
    
    #@Memoize
    def fiborecur(self,n):
        
        if n== 0:
            return 0
        if n == 1:
            return 1
        
        return self.fiborecur(n-1)+ self.fiborecur(n-2)
    
     
    def memoize(self,fn,arg):
        
        memo = {}
        if arg not in memo:
            memo[arg] = fn(arg)
        
        return memo[arg]
    
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
            return self.memo[args]    


if __name__ == '__main__':
    
    obj = Memoization()
    
    i=1
    while i < 7:
        
        #Using the simple loop method
        #fibm = obj.memoize(obj.fib,i)
        
        #Using the recurssive method
        #fibm = obj.memoize(obj.fiborecur, i)
        
        #Using a class decorator to print memoization
        fibm = obj.fiborecur(i)
        print fibm
        i += 1
   