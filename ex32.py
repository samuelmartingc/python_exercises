the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'appricots']
change = [1, 'pennies', 2, 'dimes', 3 , 'quarters']

#this is first kind of for-loops goes through a list
for number in the_count:
    print "This is count %d " % number

#same as above
for fruit in fruits:
    print "A fruit of type %s" % fruit

# also we can go through mixed list too
for i in change:
    print "I got %r in " % i

# we can also build list, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list" % i
    elements.append(i)

for i in elements:
    print "Element was %d" % i
