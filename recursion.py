'''
def fact(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n*fact(n-1)
    
a =fact(int(input("enter :")))
print(a)
'''


'''
def first():
    print("first")

def second():
    print("second")
    first()

def third():
    print("third")
    second()

third()
'''


sakthi = True

try:
    print(5/2)
    print(sakthi)

except  Exception as error:
    print("something went wrong",error)


else:
    print("error")

finally:
    print("no error")
