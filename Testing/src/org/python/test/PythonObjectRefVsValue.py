def func(list):
    print list
    list += [11, 47]
    print list
    

fibo = [1,1,2,3,5,8]
fibo1 = [1,1,2,3,5,8]
func(fibo)
#Pass by object reference hence fibo is changed too
print fibo

#fix the problem with shallow copy
func(fibo1[:])
print fibo1