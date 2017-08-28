from sys import argv

script = "null"
first = "yksi"
second = "kaksi"
third = "kolme"
fourth = "nelja"

try:
    script, first, second, third, fourth = argv
except ValueError:
    print "Not enough arguments for the script to run!"

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third
print "The fourth variable is:", fourth
