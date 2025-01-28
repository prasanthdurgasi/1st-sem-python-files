#1.Python Functions
print("1.Python Functions")
def my_function():
    print("Hi from Function")
    
my_function()
#2.using Arguments
print("2.using Arguments")
def this_function(fname):
    print(fname + " is a Gentle man")
    
this_function("Prasanth")
this_function("Ravi")
this_function("Ajay")
#3.using no of Arguments
print("3.using no of Arguments")
def no_function(fname,lname):
    print(fname + " got " + lname + " prize money")
    
no_function("Prasanth","1 lakh")
no_function("Ravi","2 lakh")
#4.Arbitrary Arguments, *args
print("4.Arbitrary Arguments, *args")
def arb_function(*skill):
    print("Ravi is very good in " + skill[2])
    
arb_function("Python","Java","C++")
#5.Keyword Arguments
print("5.Keyword Arguments")
def key_function(skill2,skill1,skill3):
    print("Ravi is very good in " + skill1)
    
key_function(skill1 = "Python", skill2 = "Java", skill3 = "C++")
#6.Arbitrary Keyword Arguments, **kwargs
print("6.Arbitrary Keyword Arguments, **kwargs")
def kwa_function(**skill):
    print("Ravi is very good in " + skill["skill2"] + " programming language")
    
kwa_function(skill1 = "Python", skill2 = "1", skill3 = "C++")
#7.Default Parameter Value
print("7.Default Parameter Value")
def dfault_function(skill = "Full stack"):
    print("Ravi is very good in " + skill)
    
dfault_function("Python")
dfault_function("Java")
dfault_function( )
dfault_function("C++")
#8.Passing a List as an Argument
print("8.Passing a List as an Argument")
def liarg_function(talent):
    for x in talent:
        print(x)
        
skill= ["Java","python","c++"]
liarg_function(skill)
#9.Return Values
print("9.Return Values")
def ret_function(x):
    return x ** 2
print(ret_function(10))
print(ret_function(20))
print(ret_function(30))

#10The pass Statement
print("10.using pass Statement")
def pas_function():
    pass

#Positional-Only Arguments
print("11.Positional-Only Arguments")
def poa_function(x,/):
    print(x)

poa_function(3)

#Keyword-Only Arguments
print("12.Keyword-Only Arguments")
def koa_function(*,x):
    print(x)

koa_function(x=33)

#Combine Positional-Only and Keyword-Only
print("13.Combine Positional-Only and Keyword-Only")
def cpok_function(a,b, /,*,c,d):
    print(a,b,c,d)

cpok_function(1,2,c=3,d=44)

#Recursion
print("14.Recursion")
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)