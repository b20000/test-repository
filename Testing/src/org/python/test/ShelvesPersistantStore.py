import shelve

s = shelve.open('test_shelf.db')
try:
    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
finally:
    s.close()
    
#Reading the objects from the temp. DB

s1 = shelve.open('test_shelf.db')
try:
    existing = s1['key1']
finally:
    s1.close()

print existing