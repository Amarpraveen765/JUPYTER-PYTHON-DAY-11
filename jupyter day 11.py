#!/usr/bin/env python
# coding: utf-8

# ### Regular Expressions
#   - pattern matching
#   - patterns(re) package
#   - cap symbol is used to represent the start of re
#   - Doller is used to represent the end of re
#   - [0-9] --> Any digit matching
#           -- Two digit number (^[0-9]{2}$)   
#   -- Five digit number (^[0-9]{5}$)

# In[8]:


# Function to test two digits numbers matching
import re
def twodigitmatching(n):
    pattern = '^[0-9]{2}$'
    n = str(n)
    if re.match(pattern,n):
        return True
    return False
print(twodigitmatching(12)) # True
print(twodigitmatching(123)) # False


# # Regular Expressions for character 
# 
#  * [a-z] any lower case character
#  * [A-Z] any upper case character  
#  * ^[a-z]{5}$ --> it accepts 5 lower case character
#  
#  * ^[a-zA-z]{8}$ --> it accepts 8 lower and upper case character
#  
#  * ^[a-zA-Z0-9]{8}$ --> it accepts anything upper,lower and number  character
#  

# In[9]:


# Function to define to test username having 8 character 
# Upper case and lower
def testusername(s):
    pattern = '^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testusername('GitamHYD')) 
print(testusername('Gitam188')) 


#  ### regular expression to match the indian mobile no
#  - 10 Digit
#  - (First digit will be [6-9] and remaining digits  will be form[0-9])
#  - Example 9642153215
#  - Re - ^[6-9][0-9]{9}$
#  - Example:- 09988774455
#  
#  - Re -- ^[0][6-9][0-9]{9}$
#  - Example - +919988774455
#  
#  - Re - ^[+][9][1][6-9][0-9]{9}$
#  

# In[12]:


# function to validate the indian mpbile number
def phonenumbervalidation(phone):
    pattern = '^[+][9][1][6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[6-9][0-9]{9}$'
    phone = str(phone)
    if re.match(pattern,phone):
        return True
    return False
phonenumbervalidation('9988774455')


# -- Regular expression to validate the rollnumber 
#     - Example : 1521A0501
#     - Example : 1521A0109
#     - Example : 1521A0499
#  
# -- Regular expression to validate the passward
#  
#     - parameters : len min of 6 characters and max of 15 characters
#     - Accept Lower case, upper case, digits, splchar(@ ,#,$,!)
# 
# 

# In[19]:


def rollnumbervalidation(rollnumber):
    pattern = '^[1][5][2][1][A][0-9]{4}$'
    rollnumber = str(rollnumber)
    if re.match(pattern,rollnumber):
        return True
    return False
rollnumbervalidation('1521A0499')


# In[24]:


def password(s):
    pattern = '^[!-~]{6,15}$'
    if re.match(pattern,s):
        return True
    return False
password("Ap@18151925")


# ### Email id validation using regular expression
# - Example :- username@domainname.extension
# - Username :-
#             - length will be [6-15]
#             - no spls characters apart from Underscore(_)
#             - should not begin or end with Underscore(_)
#             - character set:- all digits and lower case
# - Domainname :-
#           - length will be [3-18]
#           - no special characters
#           - characters set:- all digits and lower case
# 
# - Extension :-
#           - length will be [2-4]
#           - no special characters
#           - characters set:- lower case character    
#           
# - Re -- '^[0-9a-z][0-9a-z_.]{5,15}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'          

# In[26]:


def emailvalidation(email):
    pattern =  '^[0-9a-z][0-9a-z_.]{5,15}[@][a-z0-9]{3,18}[.][a-z]{2,4}$' 
    if re.match(pattern,email):
        return True
    return False
emailvalidation('amarpraveen02@gmail.com')


# ### turtle Graphics

# In[1]:


# step1 : make all the tirtle package to imported 
import turtle
# turtle method cretes and returns a new object 
a = turtle.Turtle()
# Forwarde() method moves 100 pixels 
turtle.forward(100)
# we are done
turtle.done()


# In[1]:


# draw in revers direction
import turtle as tt
a = tt.Turtle()
a.backward(100)
tt.done


# In[2]:


# draw square
import turtle as tt
a = tt.Turtle()
a.forward(150)
a.right(90)
a.forward(150)
a.right(90)
a.forward(150)
a.right(90)
a.forward(150)
a.right(90)
tt.done()


# In[1]:


# draw square
import turtle as tt
a = tt.Turtle()
a.backward(150)
a.left(90)
a.backward(150)
a.left(90)
a.backward(150)
a.left(90)
a.backward(150)
a.left(90)
tt.done()


# In[1]:


# draw triangle
import turtle as tt
a = tt.Turtle()
a.forward(100)
a.right(120)
a.forward(100)
a.right(120)
a.forward(100)
a.right(120)
tt.done()


# In[1]:


#loop statement
import turtle as tt
aa = tt.Turtle()
for i in range(4):
    aa.backward(150)
    aa.left(90)
tt.done()    


# In[1]:


# star
import turtle as t
a = t.Turtle()
for i in range(5):
    a.forward(50)
    a.right(144)
t.done()    


# In[1]:


# spiraling star
import turtle as t
a = t.Turtle()
a.pencolor('gold')
for i in range(40):
    a.forward(i*10)
    a.right(144)
t.done()    


# In[2]:


# square sprial help of turtle
import turtle as t
a = t.Turtle()
a.pencolor('gold')
for i in range(250):
    a.forward(i)
    a.left(91)
t.done()    


# In[7]:


# square sprial help of turtle
import turtle as t
a = t.Turtle()

for i in range(250):
    if i%2 == 0:
        a.pencolor('gold')
        a.forward(i)
        a.left(91)
    else:
        a.pencolor('blue')
        a.forward(i)
        a.left(91)
t.done()    


# In[1]:


# hexagon with multi color 
from turtle import *
colors = ['blue','green','yellow','orange','purple','red']
for x in range(360):
    pencolor(color[x%6])
    width(x/100 + 1)
    forward(x)
    left(56)


# In[1]:


# go to funcion
from turtle import *
goto(50,50)
goto(-50,50)
goto(100,-50)
goto(-50,-50)


# In[2]:


# setheading(hesding)
# will change the current direction to the heading angle
from turtle import *
colors = ['blue','green','yellow','orange','purple','red']
for angle in range(0,360,15):
    pencolor(color[angle%6])
    steheading(angle)
    forward(100)
    writ(str(angle)+ 'O')
    backward(100)


# In[4]:


# undo() function will undo the turtle last action
from turtle import *
pencolor('blue')
for i in range(15):
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
pencolor('red')
for i in range(90):
    undo()


# In[ ]:




