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


if __name__ == "__main__":
    
    obj = PythonTest();
    #print obj.addTwo(4,5)
    
    n = 5
   
    #for items in xrange(n):
        
        #print obj.fibonacci(items)
        
    #print obj.factorial(n) 
    
    print obj.pascal(n)