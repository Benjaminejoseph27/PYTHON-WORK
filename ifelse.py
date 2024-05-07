##1 TO FIND MAXIMUM BETWEEN TWO NUMBERS
'''
GO=int(input("ENTER A VALUE"))
BO=int(input("ENTER A VALUE"))
print()
if GO>BO:
    print("VALUE 1 IS GREATER")
else:
    print("VALUE 2 IS GREATER")
'''
##2 TO FIND MAXIMUM BETWEEEN THREE NUMBERS

'''
CO=int(input("ENTER A VALUE"))
PO=int(input("ENTER A VALUE"))
NO=int(input("ENTER A VALUE"))
print()
if CO>PO and CO>NO:
    print("VALUE 1 IS GREATER")
if PO>NO:
    print("VALUE 2 IS GREATER")
else:
    print("VALUE 3 IS GREATER")
'''

##3 TO CHECK WHETHER A NUMBER IS NEGATIVE , POSITIVE OR ZERO

'''
BOT=(input("ENTER A VALUE"))
print()
if BOT in "123456789":
    print("THE VALUE IS POSITIVE")
if BOT==0:
    print("THE VALUE IS ZERO")
else:
    print("THE VALUE IS NEGATIVE")
'''

##4 TO CHECK WHETHER A NUMBER IS DIVISIBLE BY 5 AND 11  

'''
JK=int(input("ENTER A VALUE"))
print()
if JK%5==0 and JK%11==0:
    print('IT IS DIVISIBLE BY 5 AND 11')
else:
    print("INVALID")

'''

####5 TO CHECK WHETHER A NUMBER IS ODD OR EVEN

'''=int(input("Enter a value:"))
if a%2==0:
     print("the value is even")
else:
     print("the value is odd")'''

##6 TO CHECK WHETHER A YEAR IS LEAP YEAR OR NOT
'''
X=int(input("Enter a year:"))
if X%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")'''

##7  TO CHECK WHETHER THE CHARACTER  IS ALPHABET  OR NOT
'''
y=input("Enter a character:")
z=y.isalpha()
if  z==True:
    print("The entered character is alphabet")
else:
    print("The entered character is not alphabet")'''

##8 TO CHECK WHETHER THE ALPHABET  IS VOWEL OR CONSONANT
'''
word=input("Enter a character:")
if word in ("AEIOUaeiou"):
    print("The entered character is vowel")
else:
    print("The entered character is consonant")'''

##9 TO CHECK WHETHER THE CHARACTER IS ALPLABET OR INTEGER OR SPECIAL CHARACTER

'''
q=input("Enter a character:")
if q in ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxzy"):
    print("The entered character is an alphabet")
if q in("0123456789"):
    print("The entered character is number")
else:
    print("The entered character is special character")
'''

##10 TO FIND  THE CHARACTER IS UPPER OR LOWER CASE

'''
C=input("Enter a character:")
if C in ("ABCDEFGHIJKLMNOPQRSTUVWXZY"):
    print("The character are in upper case")
else:
    
    print("The character are in lower case")
'''

##11 TO INPUT WEEK NUMBER AND PRINT WEEK DAY

'''
week=int(input("Enter a week number:"))
print()
if week==1:
    print("MONDAY")
if week==2:
    print("TUESDAY")
if week==3:
    print("WEDNESDAY")
if week==4:
    print("THURSDAY")
if week==5:
    print("FRIDAY")
if week==6:
    print("SATURDAY")
if week==7:
    print("SUNDAY")
if week==(" "):
 
    print("Invaild")
'''

##12 TO INPUT MONTH NUMBER AND PRINT NUMBER OF DAYS IN THAT MONTH

'''
month=int(input("ENTER A MONTH NUMBER"))
if month in[1,3,5,7,9,11]:
    print("The entered month has 31 days")
if month in[2,4,6,8,10,12]:
    print("The entered month has 30 days")
else:
    print("Invaild")
'''

##13 Money exchange sum

'''
amount=int(input("Enter the amount:"))
print()
g=amount//500
amount%=500

TW=amount//200
amount%=200

H=amount//100
amount%=100

FI=amount//50
amount%=50

TE=amount//20
amount%=20

Tents=amount//10
amount%=10

GH=amount//5
amount%=5

Two=amount//2
amount%=2

Ones=amount

print("500:",g)
print("200:",TW)
print("100:",H)
print("50:",FI)
print("20:",TE)
print("10:",Tents)
print("5:",GH)
print("2:",Two)
print("1:",Ones)

'''

##14 TO INPUT ANGLES OF A TRIANGLE IS VALID OR NOT

'''
W=input("Enter side one:")
Z=input("Enter side two:")
L=input("Enter side three:")

print("\n")
if W in "123456789":
    print("Side one  is valid")
if W=="0":
    print("Invaild")
if Z in "123456789":
    print("Side two is valid")
if Z=="0":
    print("Invaild")
if L in "123456789":
    print("Side three is vaild")
if L=="0":
    print("Invaild")
'''

##15 TO INPUT ALL SIDES OF A TRIANGLE AND CHECK WHETHER TRIANGLE IS VAILD OR NOT

'''
a=int(input("Enter angle one:"))
b=int(input("Enter angle two:"))
c=int(input("Enter angle three:"))

print("\n")
if a+b+c==180:
    print("THE TRIANGLE IS VAILD")
else:
    print("INVALID ANGLES")
'''

##16 TO CHECK WHETHER THE TRIANGLE  IS EQUILATERAL,ISOSCELES OR SCALENE TRIANGLE

'''
D=int(input("Enter side one:"))
H=int(input("Enter side two:"))
J=int(input("Enter side three:"))

if D==H==J:
    print("The triangle is equilateral")
elif D==H!=J:
    print("The triangle is isosceles")
elif D!=H!=J:
    print("THe triangle is scalene")
'''

##17 TO FIND ALL ROOTS OF A QUADRATIC EQUATION

'''
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=int(input("Enter a value:"))
delta=(b**2)-(4*a*c)
if delta>=0:
    root1=(-b+(b**2-4*a*c)/2*a)
    root2=(-b-(b**2-4*a*c)/2*a)
    print(root1)
    print(root2)
else:
    print("imaginary roots")
'''

##18 TO CALCULATE PROFIT OR LOSE

'''
G=int(input("ENTER THE PURCHASING VALUE:"))
F=int(input("ENTER THE SELLING VALUE:"))
if G<F:
    print("IT IS A PROFIT OF:")
    print(F-G)
if F<G:
    print("IT IS A LOSS OF :")
    print(G-F)
if G==F:
    print("IT IS NEITHER A PROFIT OR LOSS")
'''

##19 TO INPUT MARKS OF FIVE  SUBJECTS, CALCULATE PERCENTAGE AN GRADE 

'''
SCIENCE=int(input("ENTER YOUR PHYSCIS MARK"))
CHEMISTRY=int(input("ENTER YOUR CHEMISTRY MARK"))
BIOLOGY=int(input("ENTER YOUR BIOLOGY MARK"))
MATHEMATICS=int(input("ENTER YOUR MATHEMATICS MARK"))
COMPUTER=int(input("ENTER YOUR COMPUTER "))
if SCIENCE==CHEMISTRY==BIOLOGY==MATHEMATICS==COMPUTER>=90:
    print("GRADE A")
elif SCIENCE==CHEMISTRY==BIOLOGY==MATHEMATICS==COMPUTER>=80:
    print("GRADE B")
elif SCIENCE==CHEMISTRY==BIOLOGY==MATHEMATICS==COMPUTER>=70:
    print("GRADE C")
elif SCIENCE==CHEMISTRY==BIOLOGY==MATHEMATICS==COMPUTER>=60:
    print("GRADE D")
elif SCIENCE==CHEMISTRY==BIOLOGY==MATHEMATICS==COMPUTER>=40:
    print("GRADE E")
elif SCIENCE==CHEMISTRY==BIOLOGY==MATHEMATICS==COMPUTER<40:
    print("GRADE F")
'''

##20 

#21 amount electricity

'''
unit=int(input("Enter a electricity unit:"))
if   unit<=50:
    a=unit*0.5
    b=a*0.20
    c=a+b
    print("The amount for electricity used is: $",a)
    print("The amount of 20% electricity unit is: $",b)
    print("The amount after including 20% surcharge is: $",c)
    print("The total amount  to be paid for electricity used  is: $",c)
elif  unit<=150:
    a=(50*0.5)+(unit-50)*0.75
    b=a*0.20
    c=a+b
    print("The amount for electricity used is: $",a)
    print("The amount of 20% electricity unit is: $",b)
    print("The amount after including 20% surcharge is: $",c)
    print("The total amount  to be paid for electricity used  is: $",c)
elif unit<=250:
    a=(50*0.5)+(100*0.75)+(unit-150)*1.20
    b=a*0.20
    c=a+b
    print("The amount for electricity used is: $",a)
    print("The amount of 20% electricity unit is: $",b)
    print("The amount after including 20% surcharge is: $",c)
    print("The total amount  to be paid for electricity used  is: $",c)
else:
    a=(50*0.5)+(100*0.75)+(100*1.20)+(unit-250)*1.50
    b=a*0.20
    c=a+b
    print("The amount for electricity used is: $",a)
    print("The amount of 20% electricity unit is: $",b)
    print("The amount after including 20% surcharge is: $",c)
    print("The total amount  to be paid for electricity used  is: $",c)
'''

