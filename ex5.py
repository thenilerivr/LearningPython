#http://learnpythonthehardway.org/book/ex5.html
#Exercise 5: More Variables and Printing
#Nile Fairfield learning Python

my_name = 'Nile E. Fairfield'
my_age = 27 # not a lie
my_height = (5+11.0/12)*12 # inches
my_weight = 160 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blonde'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)