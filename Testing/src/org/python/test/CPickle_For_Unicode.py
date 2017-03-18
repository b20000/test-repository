import codecs
try:
   import cPickle as pickle
except:
   import pickle
     
str1 = u'lǘelü'
print "Pickling"
print "str1 [" + repr(str1) + "]"
str1U = str1.encode("UTF-8")
print "str1U [" + repr(str1U) + "]"
PickleStr1 = cPickle.dumps(str1U)
SPickleFile = codecs.open('SpFile.utf', 'w')
SPickleFile.write(PickleStr1)
SPickleFile.close()
     
print "\nUnpickling"
f = codecs.open('SpFile.utf', 'r')
str2U = cPickle.load(f)
print "str2U [" + repr(str2U) + "]"
str2 = str2U.decode("UTF-8")
print "str2 [" + repr(str2) + "]"

