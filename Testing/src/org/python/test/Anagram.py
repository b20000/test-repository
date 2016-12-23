

class Anagram(object):
    
    def isAnagram(self,s1, s2):
        
        s1 = s1.replace("  ", "").lower()
        s2 = s1.replace("  ", "").lower()
        
        return sorted(s1) == sorted(s2)

    def isAnagram2(self,s1,s2):
        
        pass
    
    
if __name__ == '__main__':
    
    obj = Anagram()
    print ( obj.isAnagram("client eastwood", "old west action") )