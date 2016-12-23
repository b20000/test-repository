class Stack(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def getSize(self):
        return len(self.items)
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmptry(self):
        return self.items == []
    
    def getSize(self):
        return len(self.items)
    
    def enQueue(self,item):
        self.items.insert(0,item)
    
    def deQueue(self):
        return self.items.pop()
 
class Deque(object):
    
    def __init__(self):
        self.items = []
        
    def isEmptry(self):
        return self.items == []
    
    def getSize(self):
        return len(self.items)
    
    def addFront(self,item):
        self.items.append(item)
        
    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)   
    
if __name__ == '__main__':
   
    '''
    st = Stack()
    print st.getSize()
    print st.isEmpty()
    
    st.push("hello")
    st.push("World")
    st.push(3)
    
    print st.isEmpty()
    print st.peek()
    print st.pop()
    
    print st.getSize()
    print st.peek()
    
    q = Queue()
    print q.isEmptry()
    
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    
    print q.isEmptry()
    print q.getSize()
    
    print q.deQueue()
    '''
    
    d = Deque()
    
    print d.isEmptry()
    
    d.addFront("Hello")
    d.addRear("World")
    
    print d.getSize()
    
    print d.isEmptry()
    
    print d.removeRear() + ' ' + d.removeFront()