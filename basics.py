#Here goes the basics : 

#This is a comment that starts with '#'

"""
This is a comment that contains more than one ligne and can be wroten without being compiled but not everywhere on the code .
"""


#To print on the shell .
print("hello world !")

#initiating variable 
a="A"
b="B"

#printing variables and concatenation
print("This is the variable a"+ a + "\n this is the variable b"+b+".")

#priting integer + concatenation + casting
integer =5
print('this is the integer content plus concatenation & casting '+str(integer)+'.')

#printing the type of the variables
variable=5
print(type(variable))           #that would print int that stands for integer

variable="5"                    
print(type(variable))           #that would print str that stands for string

variable = 5.5
print(type(variable))           #that would print float that stands for a floating number

variable = 5.5+5j
print(type(variable))           #that would print complex that stands for a complex number

variable=True
print(type(variable))           #that would print bool that stands for a boolean value and it's either true or false 



#Python does separate between those variables !
a=5
A=100
print(a)                        #it would print 5
print(A)                        #it would print 100

#Assign multiple values
a,b,c=4,5,6
print(a)                      #that would print 4
print(b)                      #that would print 5
print(c)                      #that would print 6

a=b=c=1
print(a)                      #that would print 1
print(b)                      #that would print 1
print(c)                      #that would print 1

#Lists
a=['a','b','c']
print(a)                      #that would print ['a','b','c']
b=c=a

#same thing with lists 

print(b)                      #that would print ['a','b','c']
print(c)                      #that would print ['a','b','c']

#importing random library and generating random numbers
import random
print(random.randrange(1, 10))        #That would generate a random number between 1 and 10

#Strings and arrays
a="hello"
print(a[0])                   #that would print h as the first element of the array , it starts with 0 and end with the length of the string minus 1
print(a[-1])                  #that would print the last element of the array

            #Same thing goes with the strings
a=[1,2,3,4]
print(a[0])                   #that would print 1
print(a[-1])                  #that would print 4

#The length of the string 
a='hello world'
print(len(a))                 #that would print 11 as the length of the string 

#the in statement 
a="hello me "
print(type("hello" in a))     #that would print bool and if i remove the type it would print true because hello is in the string a 

#the not in statement
a="hello world !"
print('azar' in a)            #that would print false because azar is not in the string of a .

#slicing 
a='hello malek'
print(a[0:-1])                #that would print hello male because the last one is not included
print(a[:-1])                 #that would do the same thing as the previous example
print(a[2:5])                 #that would print llo because the first l is at the position 2 starting with 0 and it would go to the position 5 which is the o
print(a[::1])                 #that would print hello malek it went from the beginning to the end with a step of one .
b=a[::-1]
print(b[:])                   #that would print the reverse of a which is kelam olleh

#modify a string 
a='    hello WORLD!     azar         '
print(a.upper())              #that would print     HELLO WORLD!     AZAR          it would turn all the characters to upper cases
print(a.lower())              #that would print     hello world!     azar          it would turn all the characters to lower cases
print(a.strip())              #that would print hello world azar it would remove the left and the right white spaces but not in between
print(a.replace('l','azar'))  #that would print        heazarazaro WORLD!     azar  it would replace all the  'l' with 'azar' on the string a
print(a.lower().split('o'))   #that would turn the string to lower cases and split it to a list that contains  ['        hell', ' w', 'rld!     azar         '] it would remove the o

#format strings
a="hello i'm here to "
b='demonstrate how '
c='format strings works'
print('{2} {1} {0}'.format(a,b,c))        #that would print hello i'm here to  demonstrate how  format strings works it starts with 0
print('{2} {1} {0}'.format(a,b,c))        #that would print format strings works demonstrate how  hello i'm here to  it starts with 0 but the order is not correct
print('{2} {1} {2}'.format(a,b,c))        #we can do that as well where it would print the string c twice , at the beginning and the end and the string b in the middle.












#To quit the shell
exit()
