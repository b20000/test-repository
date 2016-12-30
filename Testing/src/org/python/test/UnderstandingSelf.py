class Parent(object):
    i = 5;
    def __init__(self):
        self.i = 5

    def doStuff(self):
        print(self.i)

class Child(Parent, object):

    def __init__(self):
        super(Child, self).__init__()
        self.i = 7

class Main():

    def main(self):
        m = Child()
        print(m.i) #print 7
        m.doStuff() #print 7
        

if __name__ == '__main__':
    
    m = Main()
    m.main()