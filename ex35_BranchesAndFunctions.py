#http://learnpythonthehardway.org/book/ex35.html
#Exercise 35: Branches and Functions
#Nile Fairfield learning Python

from sys import exit
import time

def gold_room():
	print "This room is full of gold. How much did you take?"
	next = raw_input(" >")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy. YOU WIN!"
		exit(0)
	else:
		dead("YOU GREEDY BASTARD!")

def bear_room():
	print "There is a bear in here.\nHe has a bunch of honey and he is infront of another door.\nHow will you get him to move?"
	print "Options:\n\ttake honey\n\ttaunt bear\n\topen door"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			bear_moved = True
			print "The bear has moved from the door. You can open the door now."
		elif next == "taunt bear" and bear_moved:
			dead("The bear doesn't like being taunted twice and he chews your leg off.")
		elif next == "open door" and not bear_moved:
			dead("Gotta move the bear first.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "Learn to type..."
		
def cthulhu_room():
	print "The great evil Cthulhu is sitting right infront of you!\nHe looks at you are you go insane.\nDo you flee for your life or eat your own hand?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "ea" in next or "han" in next:
		dead("Well, at least that was tasty.")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "You're dead!"
	exit(0)
		
def start():
	print "You find yourself in a dark room.\nThere is a door to your right and your left."
	print "..."
	time.sleep(.5)
	print "..."
	time.sleep(.5)
	print "..."
	time.sleep(.5)
	print "..."
	time.sleep(.5)
	print "Do you take the left or the right?"
	
	next = raw_input(" >")
	
	if "left" in next:
		bear_room()
	elif "right" in next:
		cthulhu_room()
	else:
		dead("You stumbled in the dark until you starve to death.")

start()