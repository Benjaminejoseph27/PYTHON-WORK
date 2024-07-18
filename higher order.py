##using map() function

# =>can give two iterables and function

def name(a,b):
    return a+b

a =["sakthi","saptha",]
b =["narayanane","-ladki"]

x=map(name,a,b)
print(list(x))


##double
'''

def myfunc(n):
    return n*2

a =[96,369,16,36,39,30]
x = map(myfunc,a)
print(list(x))

##triple


def my_func(n):
    return n*3


a =[96,369,16,36,39,30]
x = map(my_func,a)
print(list(x))


##quadra


def quad(n):
    return n*4

a =[96,369,16,36,39,30]
x = map(quad,a)
print(list(x))
'''



##using filter() function 

# => Only one iterable can given

'''
## vote eligible


def myFunc(x):
    if x >= 18:
        return True
    else:
        return False


ages =[5,12,17,18,22,30]

vote_eligible = filter(myFunc, ages)

print(list(vote_eligible))


## divisible of no

def division(x):
    if x % 5 ==0:
        return True
    else :
        return False

num =[12,20,36,45,52,60,71,89,90]

x =filter(division,num)

print(list(x))

'''
    
## using Reduce() function

import functools

lis = [1, 3, 5, 6, 2]

print("The sum of the list elements is : ", end="")

print(functools.reduce(lambda a, b: a+b, lis))


from functools import reduce


l=[1,2,3,4,5]

def sum(acc , currentvalue):
    print("acc",acc)
    print("currentvalue",currentvalue)
    return acc + currentvalue


reduce(sum,l)
