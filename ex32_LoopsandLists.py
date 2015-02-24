#http://learnpythonthehardway.org/book/ex32.html
#Exercise 32: Loops and lists
#Nile Fairfield learning Python

count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this loop goes through a list
for number in count:
	print "This is the count: %d" % number

#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#also, we can go through mixed lists.
for i in change:
	print "I got %r" % i

#we can build list. Initialize an empty one first
elements = []

#then use the range function to do 0 to 5 counts. 
for i in range(0,6): #This is 0,1,2,3,4,5. Should be [0,6)
	print "Adding %d to the list." % i
	#append is a function
	elements.append(i)

#now let's print them out
for i in elements:
	print "Element was: %d" % i