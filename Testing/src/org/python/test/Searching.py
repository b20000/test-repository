from jinja2.nodes import Pos
class Searching(object):
    
    def sequential_search(self,arr,ele):
        
        last = len(arr)
        found = False
        
        for i in xrange(0,last):
        
            if arr[i] == ele:
                found = True
    
        return found
    
    def sequential_search_improvement(self,arr,ele):
        
        last = len(arr)
        found = False
        
        #Assume the array is sorted or sort the array.
        arr = sorted(arr)
        
        print arr
        
        for i in xrange(0,last):
        
            if arr[i] == ele:
                found = True
    
            else:
                if arr[i] > ele:
                    return found
                
        return found
    
    def binary_search(self, arr, ele):
        
        first = 0
        last = len(arr) - 1
        found = False
        
        #Binary search works only on sorted array
        arr = sorted(arr)
        
        
        while first <= last and not found:
            
            mid = (first+last)/2
                   
            if arr[mid] == ele:
                found = True
           
            else:
                if ele > arr[mid]:
                    first = mid + 1
                else:
                    last = mid - 1
        
        return found

if __name__ == '__main__':
    
    objSearch = Searching()
    
    arr = [1,4,7,2,3,9]
    
    #print objSearch.sequential_search(arr, 10)
    #print objSearch.sequential_search_improvement(arr, 5)
    
    print objSearch.binary_search(arr, 5)
    