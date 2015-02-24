#http://learnpythonthehardway.org/book/ex4.html
#Exercise 4: Variables And Names
#Nile Fairfield learning Python

#initialize cars to integer 100
cars = 100
#initialize space_in_a_car to float 4
#each car can fit 4 passengers
space_in_a_car = 4.0
#there are 30 total drivers
drivers = 29
#there are 90 passengers
passengers = 90

#do math on variables. Variable does not need to be initialized or allocated
#there can only be one car driven by each driver
cars_not_driven = cars - drivers
#copy variables
cars_driven = drivers

#Total amount of seats available. Float
carpool_capacity = cars_driven * space_in_a_car
#avg passengers in each car will be integer
average_passengers_per_car = passengers / cars_driven
avg_psg_per_car_float=float(passengers) / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "We need to put exactly", avg_psg_per_car_float, "in each car."