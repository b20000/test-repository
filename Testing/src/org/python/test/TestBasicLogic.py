import collections


class BasicLogic(object):
    
    def reverseString(self,string):
        index = len(string)
        new_string = ''
        
        while index:
            index = index -1
            new_string += string[index]
            
        print new_string

    def printDuplicatesInAString(self, string):
        
        d = {}
        for items in string:
            
            if items not in d.keys():
                d[items] = 1
            else:
                d[items] +=1
            
        print d
        
    def removeDuplicatesInAString(self, string):
        
        new_String = []
        for items in string:
            
            if items not in new_String:
                new_String.append(items) 
            
            
        print ''.join(new_String)
        
    def printVowlesAndConsonants(self,string):
        
        vowels = 'aeiou'
        #consotants = 'bcdfghjklmnpqrstvwxyz'
        
        vC = 0
        cC = 0
        
        for items in string.lower():
            if items in vowels:
                vC +=1
            else:
                cC +=1
        print "Vowels " + str(vC) + " Consonants " + str(cC)  
        
    def countUniqueChracterInAString(self,string):
        
        List  = list(string)
        print List
        Uniq = set(List)
        print Uniq
        
        for keys in Uniq:
            print keys 
            
    def compression(self,string):
        
        r = ''
        l = len(string)
        
        if l == 0:
            return ''
        
        #if l == 1:
            #print  string  + '1'
        
        last = string[0]
        count = 1
        index = 1
        
        while index < l:
            if string[index] == string [index -1]:
                count = count + 1
            else:
                r = r + string[index -1]+ str (count )
                count = 1
                
            index = index +1 
            
        print  ''.join(r+string[index-1]+ str (count) )


        
        

if __name__ == '__main__':
    
    StringA = "Hello World"
    StringB = 'AEIOU'
    objBasicLogic =  BasicLogic()
    objBasicLogic.reverseString(StringA)
    
    #Pyhton ways to do it
    print ''.join(reversed(StringA))
    print StringA[ : : -1]
    
    #Reverse an Array
    
    arr = [ 10, 2, 3, 5, 9]
    
    for items in reversed(arr):
        print items
        
    print arr [::-1]
    
    #Prints none
    print arr.reverse()
    
    objBasicLogic.printDuplicatesInAString(StringA)
    
    #Python ways
    print collections.Counter(StringA)
    
    #Removing duplicates in python ways
    print "".join(collections.OrderedDict.fromkeys(StringA))
    
    objBasicLogic.removeDuplicatesInAString(StringA)
    
    objBasicLogic.printVowlesAndConsonants(StringB)
    
    #objBasicLogic.countChracterInAString(StringA)
    
    objBasicLogic.compression('ABBCCCDDDD')