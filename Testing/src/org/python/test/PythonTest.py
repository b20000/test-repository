class PythonTest(object):
    
    
    def fibonacci( self, n):
        
        if (n == 0):
            return n
        elif( n==1):
            return n
        else:
            return self.fibonacci(n-1)+ self.fibonacci(n-2)

    def factorial(self, n):
        
        if (n == 0):
            return n
        elif( n==1):
            return n
        else:
            return self.factorial(n-1)* n
        
    def addTwo (self, n, m):
        
        return n + m
            
    def pascal(self,n):
        if n == 1:
            return [1]
        else:
            line = [1]
            previous_line = self.pascal(n-1)
            for i in range(len(previous_line)-1):
                line.append(previous_line[i] + previous_line[i+1])
            line += [1]
        return line
    
    def reverse(self, s):
        
        if len(s) <= 1:
            return s
        
        return self.reverse(s[1:]) + s[0]
    
    def permute(self, s):
        
        out = []
        if len(s) <= 1:
            out = [s]
            
        else:
            
            for i,let in enumerate(s):
                
                for perm in self.permute(s[:i] + s[i+1:]):
                    out += [let + perm]
                    
        return out 
    
    def coinMatch(self,target,coins):
        
        min_coin = target
        
        if target in coins:
            return 1
        
        else:
            
            for i in [c for c in coins if c <= target]:
                num_coins = 1 + self.coinMatch(target - i, coins)
                
                if num_coins < min_coin:
                    min_coin = num_coins
        
        return min_coin
    
    def coinMatchDynamic(self, target, coins, known_results):
        
        min_coins = target
        
        if target in coins:
            known_results[target]= 1
            return 1
        
        elif known_results[target] > 0:
            #print known_results[target]
            return known_results[target]
        
        else:
            for i in [ c for c in coins if c <= target]:
                
                num_coins = 1 + self.coinMatchDynamic(target - i, coins, known_results)
                
                #print min_coins
                #print known_results[target]
                if num_coins < min_coins:
                    min_coins = num_coins
                    known_results[target]= min_coins
                    
        return min_coins 
        
if __name__ == "__main__":
    
    obj = PythonTest();
    #print obj.addTwo(4,5)
    
    n = 5
   
    #for items in xrange(n):
        
        #print obj.fibonacci(items)
        
    #print obj.factorial(n) 
    
    #print obj.pascal(n)
    
    #print obj.reverse("Hello World")
    
    #print obj.permute("abc")
    
    #print obj.coinMatch(27, [1,5,10])
    
    target = 74
    coins = [1,5,10,25]
    known_results = [0]*(target+1)
    
    print obj.coinMatchDynamic(target, coins, known_results)
    
    