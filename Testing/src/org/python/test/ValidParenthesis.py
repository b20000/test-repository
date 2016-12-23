import PythonDataStructure
class ValidParenthesis(object):
    
    def __init__(self):
        pass
    
    def checkValid(self,s):
        
        if len(s)%2 != 0:
            return False
        
        start_paren = set('({[')
        match_paren = set([('(',')'),('{','}'),('[',']')])
        
        stack = PythonDataStructure.Stack()
        
        for paren in s:
            if paren in start_paren:
                stack.push(paren)
            else:
                if stack.getSize() == 0:
                    return False
                else:
                    
                    last_open = stack.pop()
                    
                    if (last_open,paren) not in match_paren:
                        return False
        
        return stack.getSize() == 0
            

if __name__ == '__main__':
    
    obj = ValidParenthesis()
    
    print obj.checkValid('()(){{}}[]((()))')
    print obj.checkValid('])}()(){{}}[]((([])))')