x = 100
print "1. Global x:", x
class Test(object):
    y = x
    print "2. Enclosed y:", y
    x = x + 1 
    print "3. Enclosed x:", x
    z = x

    def method(self):
        print "4. Enclosed self.x", self.x
        print "5. Global x", x
        try:
            print y
            #If you print self.y it will print since its in the scope of the class.
        except NameError, e:
            print "6.", e

    def method_local_ref(self):
        try:
            print x
        except UnboundLocalError, e:
            print "7.", e
        x = 200
        #The difference between method and method_local_ref is the assignment of x within
        #method_local_ref. If you comment x=200 , it will still print global x=100 
        print "8. Local x", x

inst = Test()
inst.method()
inst.method_local_ref()