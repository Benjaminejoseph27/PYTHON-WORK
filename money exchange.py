##Money exchange sum

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



