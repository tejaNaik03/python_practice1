#Q1:- Write a program to ckeck a character is in vowel or not.'

vow='aeiouAEIOU'
char=input("Enter the characters:-")

if char in vow:
    print("it is vowel",char)
else:
    print("it is not vowel",char)


#Q2:-Library Book usage fees:'

d=int(input("Enter the no. of days: "))
tf=0
if d<=5:
    tf=d*2
elif d>=6 and d<=10:
    tf=d*3
elif d>=11 and d<=15:
    tf=d*4
else:
    tf=d*5
print( "The total fee",tf)


#Q3:- Given an integer n, perform the following conditional actions:

n=int(input("Enter the integer: "))
if (n%2!=0):
    print('WEIRD')
elif n%2==0 and 2<=n<=5:
       print('NOT WEIRD')

elif n%2==0 and n>20:
         print('NOT WEIRD1')
