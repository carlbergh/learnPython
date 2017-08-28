name = 'Tomi Ojala Carlbergh'
age = 34.0 # not a lie
height = 182.0 # cm
weight = 74.0 # kg
wight_pounds = 0
eyes = 'Green'
teeth = 'white'
hair = 'Blonde'

def kg_to_pounds(kg):
    return kg * 2.2046

def cm_to_inches(cm):
    return cm * 1.0 / 2.54

print "Let's talk about %s." % name
print "He's %d cm tall. That will be %d inches" % (height, cm_to_inches(height))
print "He's %d kg heavy. That will be %d in pounds" % (weight, kg_to_pounds(weight))
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight,age + height + weight)
