#http://learnpythonthehardway.org/book/ex29.html
#Exercise 29: What If
#Nile Fairfield learning Python

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats!!"
	
if people > cats:
	print "Not too many cats"

if people < dogs:
	print "Too many dogs!!"
	
if people > dogs:
	print "Not too many dogs"
	
dogs += 5

if people >= dogs:
	print "People greater than or equal to dogs."

if people <= dogs:
	print "People less than or equal to dogs."

if people == dogs:
	print "People equal to dogs."