#http://learnpythonthehardway.org/book/ex24.html
#Exercise 24: More Practice
#Nile Fairfield learning Python

print 'You\'d need to know \'bout escaptes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10-2+3-6
print "This should be five: %d" % five

def secret_formula(started):
	jelly_beans = started*500
	jars = jelly_beans/1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of : %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point /= 10

print "With a starting point of : %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)