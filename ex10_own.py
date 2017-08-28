content = ['F.Massa', 'V.Bottas', 'S.Vettel', 'L.Hamilton']

table_format = "\t| %s \t|" % content

# Raw list printout
print table_format

# Print the list by loop
print "\nLoop version\n"

# Print headers first
print "| \t Drivers \t | "
print "| \t ------- \t | "

for i in content:
    print "| \t %s \t | " % i
