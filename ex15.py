from sys import argv

# Unpack the argunments to Variables
script, filename = argv

# Set default prompt
prompt = ('> ')

# Assign file to 'txt' variable
txt = open(filename)

print "Here's your file %r: " % filename

# Print file content
print txt.read()

print "Closing the file %s" % filename
txt.close()

print "Type the filename again:"

# Store new file path to new variable
file_again = raw_input(prompt)

# Open the new file path
txt_again = open(file_again)

# Print the content of the prompted file
print txt_again.read()

print "Closing the file %s" % file_again
txt_again.close()
