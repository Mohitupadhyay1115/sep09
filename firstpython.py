"""a= 5
b=6
sum=a+b
print(sum)

c= 5656
d= 654
diff= c-d
print(diff)

# relational operators

a= 50
b=52

print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a>b)
print(a<b)

# assignment operators
num =10
num= num+10

num*= 10
num-= 10
print("num:",num)


#logical operators
a= 50
b= 30
print (not False)
print (not True)
print(not(a>b))

#AND OR OPERATOR

val1= True
val2= False
print("And operator:", val1 and val2)
print("OR operator:", val1 or val2)

# type conversion
a= 2
b=4.25
sum= a+b
print(sum) 
# inputs from user, type casting

input(" enter your name:")
val =int(input(" enter some value:"))
print( type(val), val)

name = input("enter name")
age= input("enter age:")
marks= input("enter marks:")

print("welcome to duniya", name,age,marks)

str1= "list and tuple in python"

# slicing 
#str[ starting index_id : ending _idx] ending idx is not included

#print (str1[0:25])#[0:last
print(str1[-5:-1] ) """

"""
# string functions
str = "i am from studying python from apna college"
# endswith
print(str.endswith("ege")) #for serch ends word
# capitalize
print(str.capitalize())# for capitalizie one time first letter

str=str.capitalize()# modifying the string for permanent
print (str)

#replace 

#str.replace() #replaces all occurrences of old 
print (str.replace("o","a")) 


# str find (word) return 1st index of 1st occurrer

print (str.find("o"))

print (str.find("from"))

# str.count("am")# counts the occurence of substr

print(str.count("from")) """

#practice time
"""
# wap to input users first name & print its length

name= input("enter your name: ")
print("length of your name is",len(name))

# wap to find the occurrence of '$' in a string

str = "Hi, $Iam the $ symbol $99.99 , $currency "
print(str.count("$"))
 """


# CONDITIONAL STATEMENTS
  # IF-ELIF-ELSE(SYNTAX)

 # if(condtion):
  # statement....1
 # elif(condition):
# Statement2.....
  # else: 
 # statement N

  
age = (23)
if(age>= 18):
  print("can vote & apply for licence")
 elif( age<=18):  
  print("can not vote & apply for licence")



