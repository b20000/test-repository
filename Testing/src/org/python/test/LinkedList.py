from nose.tools import assert_equal
from compiler.ast import Node
from __builtin__ import None
class LinkedList(object):
    
    
    def __init__(self,node):
        self.node = node
        self.nextNode = None
    
    def checkCycle(node):
        
        marker1 = node 
        marker2 = node 
        
        while marker2 != None and marker2.nextNode != None:
            
            marker1 = marker1.nextNode
            marker2 = marker2.nextNode.nextNode
            
            if marker1 == marker2:
                return True
        
        return False

    def reverseList(head):
        
        current = head
        nextNode = None
        previous = None
        
        while current:
            
            nextNode = current.nextNode
            current.nextNode = previous
            
            previous = current
            
            current = nextNode
        return previous
    
    def nth_to_last_node(n,head):
        
        left_pointer = head
        right_pointer = head
        
        for i in xrange(n-1):
            if not right_pointer.nextNode:
                raise LookupError("Error! N node is larger than the list list.")
            
            right_pointer = right_pointer.nextNode
            
        
        while right_pointer.nextNode:
            
            left_pointer = left_pointer.nextNode
            right_pointer = right_pointer.nextNode
        
        return left_pointer

class DoublyLinkedList(object):
    
    def __init__(self,node):
        self.node = node 
        self.previousNode = None
        self.nextNode = None
                
            
''' You can define own class with different test method 
class TestCycleTest(object):
    
    def testCycle(self,sol):
        
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)
        
'''
        
if __name__ == '__main__':
    
    '''Create a cycle list first '''
    
    a = LinkedList(1)
    b = LinkedList(2)
    c = LinkedList(3)
    
    a.nextNode = b
    b.nextNode = c
    c.nextNode = a

    ''' Create a non cycle list here '''
    w = LinkedList(4)
    x = LinkedList(5)
    y = LinkedList(6)
    z = LinkedList(7)
    
    w.nextNode = x
    x.nextNode = y
    y.nextNode = z 
    
    assert_equal(LinkedList.checkCycle(a), True)
    assert_equal(LinkedList.checkCycle(x), False)
   
    print 'All test case for cycle check passed'
    
    print w.nextNode.node
    print x.nextNode.node
    print y.nextNode.node
    
    print 'Reversed the list'
    print LinkedList.reverseList(w) 
    
    print z.nextNode.node
    print y.nextNode.node
    print x.nextNode.node
                
    #assert_equal(LinkedList.nth_to_last_node(2, w),y)
    
    print 'All test case for finding nth to last node passed'