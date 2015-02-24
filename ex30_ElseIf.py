#http://learnpythonthehardway.org/book/ex29.html
#Exercise 29: What If
#Nile Fairfield learning Python

people = 20
cats = 20
dogs = 15

if people < cats:
	print "Too many cats!!"
elif people > cats:
	print "Not too many cats"
else:
	print "We can't decide about cats"

if people < dogs:
	print "Too many dogs!!"
elif people > dogs:
	print "Not too many dogs"
else:
	print "We can't decide about dogs"
	
dogs += 5

if people >= dogs:
	print "People greater than or equal to dogs."
elif people <= dogs:
	print "People less than or equal to dogs."
elif people == dogs:
	print "People equal to dogs."

if people == cats and not(cats < dogs):
	print "same number of people and cats is not less than number of dogs."
else:
	print "NOT - same number of people and cats is not less than number of dogs."