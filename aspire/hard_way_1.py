# -*- coding: utf-8 -*-

#print ('i will now count my chickens:')

#print ("Hens", 25 + 30 / 6)
#print ("Roosters", 100 - 25 * 3 % 4)

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("there are", cars, "cars available.")
print ("there are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today")