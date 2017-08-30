from sys import argv

script, filename = argv
valid_aswers = ['a', 'w']
prompt = 'a or w ? > '

print "We are going to erase %r." % filename
#print "If you don't want that, hit Ctrl-C (^C)."
#print "If you really want to erase content of the file %s?" % filename
print "Do you want to append (a) or overwrite (w) the file?"

while True:
    try:
        answer = raw_input(prompt)

        if answer not in valid_aswers:
            print "Bad choice!"
        else:
            break
    except:
        print "Enter valid answer (a/w)!"

print "Opening the file..."
# Store the fileobject in target variable
target = open(filename, answer)

# if not answer == 'a':
#      print "Truncating the file, goodbye!"
#      target.truncate()
# else:
#      print "Keeping file as is."

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

combined_text = line1 + '\n' + line2+ '\n'  + line3 + '\n'

print "I'm going to write these to the file %s." % filename

target.write(combined_text)

# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

print "And finally close it."
target.close()
