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

text = 'interactive python notebook'
print(text[1:4])

text = text.replace('notebook','nb')
print(text)

text = '   interactive python notebook   '
print(f'Before Strip : {text}')
print(f'After Strip : {text.strip()}')


#List, denoted as []
technology = ["Python","AWS","Java","AIML"]
print(f'Technologies : {technology}')
technology.append("Javasript")
print(f'Technologies After Append : {technology}')

nums = [20,10,30,5,2,10]
print(nums)
print(f'nums size : {len(nums)}')
print(f'nums sum : {sum(nums)}')
print(max(nums))
#print(min(nums))

nums.reverse()
print(nums)

nums.sort()
print(nums)


# Tuple, denoted as ()
tuple_first = (100,420,30,140,250)
print(tuple_first)
print(type(tuple_first))

#adding another object to tuple
temp = (4,5)

tuple_first +=temp

print(f'Changed tuple is : {tuple_first}')


#Set, denoted as {}

setEx = {"P1", "P2","P5","P4","P3","P2","P5"}
print(f'SET is :{setEx}')
setEx.add("P6")
print(f'Modified SET is :{setEx}')

setEx.update(["P9","P8"])
print(f'Modified  SET is  with multipe :{setEx}')



#Dictionary

emp_dic = { 
            "name" : "XYZ",
            "age" : 30,
            "desgn" : "Manager",
            "salary" : 60000.00
}

print(emp_dic)
print(type(emp_dic))

print(emp_dic["name"])
print(emp_dic.get("name"))

emp_dic["pan_no"] = "ANAJ67KHKJ"
print(emp_dic)

# Remove 
# pop 
emp_dic.pop("pan_no")
print(emp_dic)