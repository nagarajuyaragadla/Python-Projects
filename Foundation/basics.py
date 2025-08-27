#name = input('Enter Name : ')
#print(f'Welcome to python Mr.{name}')

print('---------------------')

x = 123
print(f'x : {x}')
print(f'x type of {type(x)}')

print('---------------------')

y = 123.345
print(f'y : {y}')
print(f'y of type {type(y)}')

print('---------------------')

a=4
b=7j
print(f'a+b = {a+b}')
print(f'a+b of type {type(a+b)}')
print('---------------------')

a=4+5j
b=5+6j
print(f'a+b = {a+b}')
print(f'a+b of type {type(a+b)}')
print('---------------------')

val = True
print(f'value is {val}')
print(f'value of type {type(val)}')
print('---------------------')

nonVal = None
print(f'nonVal : {nonVal}')
print(f'of type : {type(nonVal)}')
print('---------------------')

name = 'Nag'
print(f'name is {name}')
print(f'name of type is {type(name)}')
print('---------------------')

str1 = '''String with the tripple quotes.
This string is a multi line string.'''
print(str1)
print(type(str1))
print('---------------------')

designation = 'PMTS'
print(f'Name is {name} , Designation is {designation}')
print('---------------------')

#Assigning multiple values to multiple variables
a,b,c = 10,20,30
print(a+b)
print(b+c)
print(c+a)

#Object Identity
#The built-in id() function, is used to identify the object identifier

a = 'Python'  
b = a  
print(id(a))  
print(id(b))  
print(a, b)  
# Reassigned variable a  
a = 123  
print(id(a))  
print(a, b) 

# Operators
a,b = 17,3

print(f'(a+b) = {a+b}')
print(f'(a-b) = {a-b}')
print(f'(a-1) = {a-1}')
print(f'(a*b) = {a*b}')
print(f'(a/b) = {a/b}')
print(f'(a//b) = {a//b}') #devision
print(f'(a%b) = {a%b}') # moduler
print(f'(a**b) = {a**b}') #power of

a,b = True,False
print(a and b)
print(a or b)

# Program to demoncsstrate conditional operator
a, b = 30, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(f'Minimum value : {min}')

