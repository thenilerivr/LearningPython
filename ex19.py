#http://learnpythonthehardway.org/book/ex19.html
#Exercise 19: Functions and Variables
#Nile Fairfield learning Python

#The variables in your function are not connected to the variables in your script

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %.2f boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too: "
cheese_and_crackers(10+20, 5+6)

print "We can combine variables and math:"
cheese_and_crackers(amount_of_cheese+5,float(amount_of_crackers)/7)