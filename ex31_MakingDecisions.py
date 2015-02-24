#http://learnpythonthehardway.org/book/ex31.html
#Exercise 31: Making Decisions
#Nile Fairfield learning Python

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

#Get the input for door
door = raw_input("> ")

#If the user entered option 1
if door == "1": 
	print "Nile wants you to brew your beer so he can have some."
	print "1. Brew the beer and share it with Nile."
	print "2. Brew your beer and drink it all yourself."
	print "3. Don't brew it."
	
	beer_choice = raw_input("> ") #get the input for beer_choice
	
	#If the user entered option 1
	if beer_choice == "1":
		print "Nice choice, you have 5 gallons of excellent, hoppy IPA to share with your friends."
	elif beer_choice == "2":
		print "Woah dude, you got super sick! Good thing Nile is such a good friend and took care of you."
	elif beer_choice == "3":
		print "Shame on you. So lazy..."
	else:
		print "Why don't you try again, it's not that hard... just 1, 2, or 3."
	
elif door == "2":
	print "Door 1 is better..."

else:
	print "Why don't you try again, it's not that hard... just 1 or 2."
