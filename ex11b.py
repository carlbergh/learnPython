#import sys
#print "\n", sys.version
from random import randrange

guess_count = 0
answer = randrange(1,14)

while True:
    try:
        guess = int(raw_input("Guess the lucky number! (1-14): "))
        if not 0 < guess < 15:
            print "Bad number, RTFM!"
        else:
            print "Your guess is %r." % guess
            guess_count += 1

            if guess == answer:
                print "\nYou are a winner! The lucky number is (%d)" % (answer)
                print "You made it in %d guess(es)\n" % guess_count
                break
            elif guess < answer:
                print "Try a higher number!"
            elif guess > answer:
                print "Try a lower number!"
            else:
                print "Try AGAIN: "
    except ValueError:
        print "This is not a number! TRY AGAIN!!!"

# # Some functions
# def gold_room():
#     print "This room is full of gold. How much do you take?"
#
#     next = raw_input("> ")
#     if int(next) in range(50):
#         how_much = int(next)
#     else:
#         print "Man, learn how to type a number!"
#
#     if how_much < 50:
#         print "Nice, you're not greedy. You WIN!"
#         exit(0)
#     else:
#         print "Dead! You greedy bastard!"
