"""#Indentation
a = 10
b = 6

if a < b:
    print("a is less than b") #here we cannot write print excatly below of if statement, we have to give some space to it, this is called indentation in python.
                              #In python we can use either space or tab for indentation but we cannot use both of them in the same program, it will give us error.
    print(a) #here if we need to write another print, than we need to write it bleow the first print. we cannot write it with more space

if a > b:
    print("a is greater than b")

print("Hello World");print("Welcome to Python Programming")#write multiple line in single line with (;), prefer not to use it.

print("hello",end=" ") #end=" " used to print multiple line in one line.
print("I am doad")

a = 10
b = 'doad'
print(type(a))
print(type(b)) #it will show the data type of the variable."""

######### Global variable ########
x = 'global variable'

def fun1():
    x = 'local variable'           #It not change the global variable value
    global y
    y = 'global variable'          #This is the global variable inside the function
    print('This is a '+ x)

fun1()
print('This is a '+ x)
print('This is a '+ y)             #if we declear global within the function. then we use the variable outside the function


