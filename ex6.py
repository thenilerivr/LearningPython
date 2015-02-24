#http://learnpythonthehardway.org/book/ex6.html
#EExercise 6: Strings and Text
#Nile Fairfield learning Python

#Python knows you want something to be a string when you put either " (double-quotes) or ' (single-quotes) around the text.

#use format characters in creation of a variable
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

#separate inputs for format characters in parenthesis with comma
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users. The output includes the '
print "I said: %r." % x
print "I also said: '%s'." % y #you can use single quotes inside of double quotes

print "\n"
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Printing the string as an input to the print statement
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
