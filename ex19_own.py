import random

colors = ['hearts', 'clover', 'spades', 'diamonds' ]
numbers = range(2, 15)
pictures = ['knight', 'queen', 'king', 'ace']
deck = []
number_of_players = 1
credits = 10
playagain = True

def create_deck():
    deck [:]= []
    for color in colors:
        for number in numbers:
            deck.append([number, color])
        #for picture in pictures:
            #deck.append([picture, color])
    print "Deck of cards created. %d" % len(deck)
    #print deck
    return deck

def shuffle_deck():
    random.shuffle(deck)
    print "Deck of cards shuffled.\n"
    #print deck
    return deck

def decrease_credits(credits):
    credits -= credits
    return credits

def start_cards(deck, credits):
    print credits
    player_cards = []
    decrease_credits(credits)
    player_card_count = len(player_cards)

    print """\n\n
     Welcome to this amazing black jack game!
     Enjoy the game!
     You now have %d credits\n\n
     """ % credits

    for i, c in list(enumerate(deck)):
        while len(player_cards) < 2:
            player_cards.append(deck.pop(i))
    print "Player has following cards (%d):\n%r \n" % (len(player_cards), player_cards)
    print "In deck there are (%d) cards left: \n%r" % (len(deck), deck)
    return player_cards

def calculate_summ(cards):
    summ = 0
    cardcounter = 0
    for val, i in list(enumerate(cards)):
        summ = summ + cards[cardcounter][0]
        cardcounter += 1

    if summ == 21:
        print "21! You Win"
        collect_wins(summ, credits)
    elif summ <= 21:
        print " summ of cards: %d" % summ
        collect_wins(summ, credits)
    else:
        collect_wins(summ, credits)
    return credits

def check_cards(deck):
    print "(%d): \n%r\n" % (len(deck), deck)

def hit_card(player_cards, deck):
    print "\n ### Player now has\n %r " % player_cards
    summ = calculate_summ(player_cards)
    stand = ''

    while stand != 's':
        stand = raw_input(" Hit or stand (h/s)")
        if stand != 's':
            player_cards.append(deck.pop(len(player_cards)))
            print " %r\n" % player_cards

            summ = calculate_summ(player_cards)
        else:
            break

def collect_wins(summ, credits):
    print " Collecting wins? %r" % summ
    if summ in range(17, 22):
        if summ == 17:
            credits += 1
        elif summ == 18:
            credits += 2
        elif summ == 19:
            credits += 3
        elif summ == 20:
            credits += 5
        elif summ == 21:
            credits += 10
    else:
        print " No win. No new credits\n"
    return credits

while playagain:
    create_deck()
    shuffle_deck()
    player_cards = start_cards(deck, credits)

    hit_card(player_cards, deck)
    playagain = raw_input(" Play again? ")

    if playagain == 'y':
        playagain = True
        print playagain
    else:
        print " Exit game!"
        playagain = False
        print playagain
        exit(0)
#calculate_summ(player_cards)
#calculate_summ(dealer_cards)

#check_cards(deck)
