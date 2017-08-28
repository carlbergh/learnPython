print "I will now count my chickens: "

# Hens are counted by first dividing 30 / 6 giving 25 + 5 = 30
print "Hens", 25 + (30.0 / 6.0)

# Roosters are counted by 100 - (75 % 4) => 100 - 3 = 97
print "Roosters", 100 - 25 * 3.0 % 4.0

print "Now I will count the eggs:"

# Eggs are counted by first running division and %
# Giving 3 + 2 + 1 - 5 + 0 - 0 + 6
# When setting floating numbers the result will be more accurate
# 3 + 2 + 1 - 5 + 0 - 0.25 + 6
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4.0 + 6

# Trying to check i 5 is less than -2
print "Is it true that 3 + 2 < 5 - 7"
print 3 + 2 < 5 - 7

# Simple addition and subtraction
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's false."

print "How about some more."

# Checking usage of more and less than operators
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
