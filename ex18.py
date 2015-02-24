#http://learnpythonthehardway.org/book/ex18.html
#Exercise 18: Names, Variables, Code, Functions
#Nile Fairfield learning Python

#First define the functions using def
#Use : to mark the beginning of the function
#Use indentation to mark the length of the function

# This one is like your scripts with argv. It takes two arguments and unpacks them
def print_two(*args):
	arg1, arg2 = args #unpacking by having multiple variables on the left of =
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#ok, that *args is actually pointless, we can just do this. This takes two arguments directly
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#This one takes one arg
def print_one(arg1):
	print "arg1: %r" % (arg1)
	
#This one takes no arg
def print_none():
	print "I got nothin"

#Then call the functions with arguments
	
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()