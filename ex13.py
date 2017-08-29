from sys import argv

# Variables
number_of_variables = len(argv) - 1

# Definition of functions
def usage():
    print "\n1 Please provide correct number of paramerters! (2)"
    print argv, "\n"
    exit(1)

# Check number of arguments

if len(argv) > 3:
    usage()
else:
    try:
        script, age, length = argv
    except ValueError:
        print "Not enough arguments for the script to run!"

name = raw_input("Also give me your name: ")

print "Hi %r, so you are %r years old and are %r tall?" % (name, age, length)

# print "The script is called:", script
# print "The first variable is:", first
# print "The second variable is:", second
# print "The third variable is:", third
# print "The fourth variable is:", fourth
