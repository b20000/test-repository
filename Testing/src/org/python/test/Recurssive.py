from cmath import phase
class Recurssive(object):
    
    def fibonacci(self,n):
          
        if (n == 0):
            return n
        elif( n==1):
            return n
        else:
            return self.fibonacci(n-1)+ self.fibonacci(n-2)
    
       
    def factorial( self,n):
            
        if (n == 0):
            return n
        elif( n==1):
            return n
        else:
            return self.factorial(n-1)* n
    
    def sum_digits(self, n):
        
        if len(str(n)) == 1:
            return n
        else:
            return n%10 + self.sum_digits(n/10)


    def word_split(self,phrase,list_of_words, output=None):
        
        if output is None:
            output = []
            
        for word in list_of_words:
            
            if phrase.startswith(word):
                
                output.append(word)
                
                return self.word_split(phrase[len(word):], list_of_words, output)
                
        return output
     
    def reverseString(self,string):
        
        if len(string) == 1:
            return string
        
        return self.reverseString(string[1:]) + string[0]
    
      
if __name__ == '__main__':
    

    for items in xrange(5):
        print Recurssive().fibonacci(items)
        
    print Recurssive().factorial(5)
    
    print Recurssive().sum_digits(4321)
    
    print Recurssive().word_split("ilovethedog", ['why','i','the','love','dog'])
    
    print Recurssive().reverseString("Hello World")
    
    