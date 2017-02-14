#!/usr/bin/python

# Import built-in module math
import math
import ast

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print Money
AddMoney()
print Money

#=========================

content = dir(math)

#print content

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )

print ast.literal_eval("545.2222")
#Below will throw error in python 2.7
#print ast.literal_eval("1+1")


def multipliers():
  return [lambda x : i * x for i in range(4)]
    
def multipliers1():
  return [lambda x, i=i : i * x for i in range(4)]

print [m(2) for m in multipliers1()]


def extendList(val, list=[]):
    #Initialize an empty list here so that you get the desired result.
    #list = []
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

# Excellent example to understand parent child relationship.
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

#Excellent example to understand // as it always does integer division in python 2.
def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

#Understanding the behavoir of List , no index error. Empty list
list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

#Another interesting one

list = [ [ ] ] * 5

#Comment different assignment and see the behavoir. 

list[0].append(10)
list[1].append(20)
list.append(30)

print list

# Printing only the even number in the even index position.
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
print [x for x in list[::2] if x%2 ==0]


#It will throw an error since child has no attribute o1.
class father:

    def __init__(self, param):
        self.o1 = param

class child(father):

    def __init__(self, param):
        self.o2 = param

obj = child(22)
#print "%d %d" % (obj.o1, obj.o2)


class tester:

    def __init__(self, id):

        self.id = str(id)
        id="224"

temp = tester(12)
print temp.id

help(round)