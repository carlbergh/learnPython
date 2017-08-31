# This one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."

print_two('Tomi','Carlbergh')
print_two_again('Tomi','Carlbergh')
print_one('Tomi')
print_none()
