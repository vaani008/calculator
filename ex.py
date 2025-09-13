#age calculator
#x="vani"
"""y=input("enter your name:")
#if x==y:
a=int(input("May I know your age:"))
b=int(input("and also the current year:"))
print("which year were you born:",b-a)
c=100-a
print("your age 100 later:",c+b)

#positve-negative calculator
a=int(input("enter your number:"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")"""
    
"""#weather
a=input("How's your weather:")
if a=="sunny":
    print("yz i hope you wont get tanned")
elif a=="rainy":
 x=input( ("so did u carry umbrella?"))
 if x == "yes":
     print("great")
 else:
     print("its ok buy one")
     """


"""#calculator
print("calculator")
a=int(input("enter your 1st digit:"))
b=int(input("enter your 2nd digit:"))
print("in this calculator we will be having :")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exit")
x=['1','2','3','4','5']
c=int(input("please choose from (1-5):"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4 :
    
    if b==0:
        print("divison by 0 is not possible")
    else:
        print(a/b)
elif c==5:
        print("exiting the calculator")
else:
    print("invalid")"""

"""#for pets
pet={ 
     "name":"yeotan",
     "type":"dog",
      "age":"9",
      "fav food":"chicken"
      }
print(pet["name"])
pet["fav food"]="bones"
del pet["age"]
print(pet)"""

"""#age in months
a=int(input("enter the year you're born:"))
b=int(input("enter the current year:"))
c=b-a
if a>b:
   print("please check the data")


elif a<b:
    print("now you're",c,"years old")
x=int(input("enter youre birth month:"))
y=int(input("enter youre current month:"))
d=y-x
e=x-y
if y>x:
 print("your",(c*12)+d,"moths old")
elif x>y:
 print("your",(c*12)-e,"months old")"""
 
 
 
 
"""a=input("enter your fav fruits:")
fruits=a.split()
for x in fruits:
 print(fruits)"""            
 
 #factorial calculator
"""print("welcome")
a=int(input("enter the number:"))
if a==0:
    print("factorial of zero is 1")
elif a<0:
    print("it cant be negative")
else:
    factorial=1
    for i in range(1,a+1):
        factorial *=i
        print(f"the factorial of {a} is {factorial}")"""
        
#sum of 1 to 100    
"""sum=0
for i in range (1,101):
    sum+=i
    print("sum:",sum)"""
    
#tables
"""a=int(input("enter the number:"))
b=int(input("enter the value u want the table to print:"))
for i in range(1,b+1):
    print(f"{a}*{i}={a*i}")"""
    
#guessing type 1
"""s=7

while s==7:
    a=int(input("enter the guessing number:"))
    if s>a:
        print("too low")
      
    elif a>s:
        print("too high ")
      
    elif a==s:
        print("yes u did it")"""
    
#guessing type 2
"""s=7
a=0
while a!=s:
    a=int(input("enter the guessing number:"))
    if s>a:
        print("too low")
      
    elif a>s:
        print("too high ")
      
    else:
        print("yes u did it")"""
# print digits ulta
"""num = 1234
while num > 0:
    digit = num // 10
    print(num % 10, end='')
    num = digit"""

#reverse string
"""s=input("enter the word and see magic:")
reversed_str=s[::-1]
print(reversed_str)"""

"""a=input("enter a word:").lower()
#b=['a','e','i','o','u']
vowels="aeiou"
count=0
for char in a:
    if char in vowels:
        count +=1
 """
#palindrome checking
"""a=input("enter a word:").lower
if a==a[::-1]:
    print("it is palindrome")
else:
    print("its not")"""



a=(input("enter a word"))
b=(input("enter a word"))

set1=a
set2=b
if sorted(set1)==sorted(set2):
    print("yes")
else:
    print("no")

print("HEHEHE OMG OMG SOO MUCH CODE WAAAW")
    



 
