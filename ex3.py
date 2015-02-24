#http://learnpythonthehardway.org/book/ex3.html
#Exercise 3: Numbers and Math
#Nile Fairfield learning Python

print "I will now count my chickens:"

#Notice that the , concatenates strings
print "Hens", 25+30/6 #you don't need spaces, but can add them

#
print "Roosters", 100 - 25 * 3 % 4 #3%4 is 3/4=0R3=3
print "What does the % do? ", 25 * 3 % 5

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

#Why does / (divide) round down?
#It's not really rounding down; it's just dropping the fractional part after the decimal. Try doing 7.0 / 4.0 and compare it to 7 / 4 and you'll see the difference.
print 7/4
print 7.0/4