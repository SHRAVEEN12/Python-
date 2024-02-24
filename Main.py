'''print("Hello world")
print(56)'''

**********************************************************************************************************************************
#print("Hey i am a \"good boy\"and \nthis viewer is also a good boy/girl")
#print("hey", 6,7, sep =",", end="009\n")
'''a = 1234
c = 12.34
d=True
e=None
print(a)
print(c)
print(d)
print(e)
b = "harry"
print(b)
print(a,b)
print(8+0j)'''
"""print(15+8)
print(15-8)
print(15*8)
print(15/8)
print(15%8)
print(15**8)
print(15//8)"""
'''a = "1"
b = "3"
a1 = int(a)
a2 = int(b)
print(a1+a2)'''

**********************************************************************************************************************************
#input function
'''a=input()
print("my name is " + a)'''
'''a ="Harry"
b ="Shraveen"
print(a,"is brother to", b)
print(a[0])
print(a[1])
#printing in for loop 
for i in a:
  print(i)'''
'''name = "shraveenisagoodboy"
print(len(name))
print(name[9])
print(name[0:8])
print(name[-10:-3])
nm ="harry"
print(nm[-4:-2])'''
**********************************************************************************************************************************

#STRING METHODS
'''a = "shraveen"
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip("s"))
print(a.rstrip("en"))
#a = a.replace("h", "")
#print(a)
#a = a.replace("s", "p")
#print(a)
print(a.capitalize())
str1 = "Welcome to the Console!!!"
print(str1.center(50))
print(str1.center(50,"."))
print(a.count("e"))
print(a.endswith("n"))
print(a.find("e"))
print(a.index("n")) #-->gives an error when the index is not present
print(str1.isalnum())
str2 = "Welcome\n"
print(str2.isalpha())
print(a.islower())
print(a.isprintable())
print(str2.isprintable())
str3 =" "
print(str3.isspace())
str1 = "World Health Organization" 
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
str1 = "Python is a Interpreted Language" 
print(str1.startswith("P"))
str1 = "python Is A interpreted language" 
print(str1.swapcase())
str1 = "I haven'T learnt python before"
print(str1.title())'''
**********************************************************************************************************************************

#IF/ELSE statement
'''a = int(input("Enter your Age\n"))
#num =int(input("Enter the swimming license no: "))
if (a>=20):
  print("you can swim\n")
else:
  print("you cannot swim\n")

print("Go to Swimming pool if YES")'''
**********************************************************************************************************************************

#ELIF
'''a = int(input("Enter your Age\n"))
if (a>=20 and a<=30):
  print("you can swim\n")
elif (a>=30 and a<=50):
  print("You can swim upto 30 meters only")
elif (a>50 and a<=60):
  print("you can swim upto 10 meters")
else:
  print("you cannot swim\n")'''
**********************************************************************************************************************************

#NESTED IF
'''num = int(input("Enter the number"))
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")'''
**********************************************************************************************************************************

#match case statements
'''x = int(input("Enter the number\n"))
match x:
    case 0:
        print("x is zero")   
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")   
    case _ if x < 10:
        print("x is < 10")  
    case _:
        print(x)'''
**********************************************************************************************************************************

#FOR LOOP
'''num = int(input("enter the number\n"))
for i in range(num):
  print(i+1)

fruits = ["apple", "banana", "mango"]
for c in fruits:
  print(c)'''
**********************************************************************************************************************************

#while loops
'''i=int(input("enter the number"))
num =int(input("Enter the number\n"))
while (i < num):
  print(i)
  i = i+1
else:
  print("choose the correct number")'''
**********************************************************************************************************************************

#Break and continue
'''num = int(input("Enter the number\n"))
for i in range(1,100):
  print(num ,"x", i, "=" , num*i)
  if (i==10):
    continue
  elif (i==20):
    break'''
**********************************************************************************************************************************

#functions in python
# def name(a,b):
#   print("My name is" , a , b)
'''def myfunc():
  num1 = int(input("Enter the first number\n"))
  num2 = int(input("Enter the second number\n"))
  
  sum1 = num1+num2
  sum2 = num1-num2
  sum3 = num1*num2
  sum4 = num1/num2
  #(sum1+sum2+sum3+sum4)/2
  
  if sum1<sum2:
    print("Choose sum1")
  elif sum3>sum4:
    print("Choose sum2")
  else:
    print("Do not choose th less number")
#function call 
myfunc()
#name("Shraveen", "rai")'''
********************************************************************************************************************************** 
#FUNCTION ARGUMENTS
'''#Default arguments:
def func1(fname , mname="r", Lname="rai"):
  print("Hello my name is ", fname , mname, Lname)
func1("Shraveen")

#Keyword arguments
def func2(fname , mname, Lname):
  print("Hello my name is ", fname , mname, Lname)
func2(Lname="rai" , fname="Shraveen" , mname="r")

#Required arguments
def func3(fname , mname, Lname):
  print("Hello my name is ", fname , mname, Lname)
func3("Shraveen" , "r", "rai") #---> all arguments are required

#Variable length arguments
def func4(*name):
  print("Hello my name is",name[0],name[1],name[2],name[3])
func4("","Shraveen","r","rai")

#Default arguments:
def func1(fname , mname, Lname):
  return (fname , mname, Lname)
print("Shraveen", "r", "rai")'''
**********************************************************************************************************************************

#lists
'''list1 = ["apple","banana","chikku"]
list2 = [1,2,3,4]
print(list1)
print(list2)'''

# list indexes
'''colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[4])

#Positive Indexing:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

#Negative Indexing:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])'''
**********************************************************************************************************************************

'''# list methods
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)

colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

colors = ["voilet", "green", "indigo", "blue", "green"]
m=colors.index("indigo")
print(m)
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
y=num.index(2)
print(y)

colors = ["voilet", "green", "indigo", "blue", "green"]
c=colors.count("blue")
print(c)
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(1))

colors = ["voilet", "green", "indigo", "blue"]
B=colors.copy()
print(B)

colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(colors)
print(colors)

#adding two lists
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
#print(colors + colors2)

colors.remove("voilet")
print(colors)'''
**********************************************************************************************************************************

'''tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

#tuple methods
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]

# positive indexing 
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]     
print(country[0])
print(country[1])
print(country[2])

#negative indexing
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes'''
**********************************************************************************************************************************

#Tuple methods
# tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# # res = tuple1.count(3)
# # res = tuple1.index(3)
# # res = tuple1.index(311)
# # res = tuple1.index(3, 4, 8)
# res = len(tuple1)
# print('Count of 3 in tuple1 is:', res)





