#http://learnpythonthehardway.org/book/ex33.html
#Exercise 33: While
#Nile Fairfield learning Python

# Make sure that you use while-loops sparingly. Usually a for-loop is better.
# Review your while statements and make sure that the thing you are testing will become False at some point.
# When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.
import datetime

def loopit(max):
	i = 0
	numbers = []
	while i < max:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		print datetime.datetime.now()
	
	print "The numbers: "

	for j in numbers:
		print j
	
max = input("How many times do you want to loop?")
loopit(max)