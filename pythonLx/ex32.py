the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges','pears','apricots']
change = [1 , 'pennies' , 2 , 'dimes' , 3 , 'quarters']

for number in the_count:
	print "the_count : %s" % number

for fruit in fruits:
	print "fruits : %s " % fruit
	
for i in change :
	print "change : %s" % i

elements = []
for i in range(0,6):
	print " i : %s" % i 
	elements.append(i)
	
for i in elements:
	print "elements : %s " %i