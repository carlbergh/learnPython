# Number of cars
cars = 100
# Space in each car
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# Cars that are available
cars_not_driven = cars - drivers
# Cars that will be driven
cars_driven = drivers
# Total amount of seats for all used cars
carpool_capacity = cars_driven * space_in_a_car
# How many passangers needs to be per car 
avarage_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", avarage_passengers_per_car, "in each car"
