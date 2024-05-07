##For loop

##1

'''
a=int(input("Enter a number:"))
for a in range(1,a,1):
    print(a)
 '''

##2

'''
b=int(input("Enter a number:"))
for b in range(b,1,1):
    print(b)
'''

##3

'''
for char in range(ord('a'), ord('z')+1):
    print(chr(char), end=" ")
'''

##4

'''
for i in range(1,100,1):
    if i % 2 == 0:
        print("Even =>",i)
'''

##5

'''
for i in range(1,100,1):
    if i % 2 != 0:
        print("Odd =>",i)
'''

##6

'''
n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n + 1):
    sum += i

print("The sum of natural numbers from 1 to", n, "is:", sum)
'''

##7

'''
n=int(input("Enter a number:"))
sum = 0
for i in range(2,n+2,2):
    sum += i
print("The sum of even numbers from 1 to",n,"is",sum)

'''

##8

'''
n=int(input("Enter a number:"))
sum = 0
for i in range(1,n+1,2):
    sum += i
print("The sum of even numbers from 1 to",n,"is",sum)
'''



##9

'''
num = int(input("Enter the number whose multiplication table you want to print: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

'''    

##10

'''
number = int(input("Enter a number: "))
count = 0
for digit in str(number):
    count += 1
print("Number of digits in", number, ":", count)
'''
