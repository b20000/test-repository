from random import randint

def dice7():
    
    return randint(1,7)

def convert7To5():
    
    roll = 7
    
    while roll > 5:
        
        roll = dice7()
        print 'dice7() produces a roll of ' , roll
    
    print 'final destination roll is ' , roll 