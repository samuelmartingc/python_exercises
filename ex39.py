# create a mapping of state to abbreviation
states = {
    'oregon' : 'or',
    'florida' : 'fl',
    'california' : 'ca',
    'new york' : 'ny',
    'michigan' : 'mi'
}

# create a basic set of states and some cities in them
cities = {
    "ca" : "san francisco",
    "mi" : "detroit",
    "fl" : "jacksonville"
}

# add some more cities
cities['ny'] = "new york"
cities['or'] = "portland"

#print out some cities
print '- ' * 10
print "NY State has: ", cities['ny']
print "OR State has: ", cities['or']

# print some states
print '- ' * 10
print "Michigan's abbreviation is: ", states['michigan']
print "Florida's abbreviation is: ", states['florida']

# do it by using the state then cities dict
print '- ' * 10
print "Michigan has: ", cities[states['michigan']]
print "Florida has: ", cities[states['florida']]

# print every state abbreviation
print '- ' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '- ' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '- ' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev])

print '- ' * 10
# safely get an abbreviation by state that might not be there
state = states.get('texas',None)

if not state:
    print "Sorry, no texas"

#get a city with default value
city = cities.get('tx','does not exist')
print "The city for the state tx is %s " % city
