# FormFire.py
# This script was written by Matt Schley as a part of the FormFire coding challenge. 
# 5/7/2014

import itertools
# uncomment the input set you would like to run from the list of four below 

combos = list(itertools.permutations([("Blue","Green"),("Blue","Yellow"),("Green","Yellow"),("Orange","Red"),("Red","Green"),("Red","Orange"),("Yellow","Blue"),("Yellow","Red"),("Red","Red")]))
#combos = list(itertools.permutations([("Blue","Green"),("Blue","Yellow"),("Red","Orange"),("Red","Green"),("Yellow","Red"),("Orange","Purple")]))
#combos = list(itertools.permutations([("Blue","Yellow"),("Red","Orange"),("Red","Green"),("Yellow","Red"),("Orange","Red")]))
#combos = list(itertools.permutations([("Blue","Green"),("Blue","Yellow"),("Green","Yellow"),("Orange","Red"),("Red","Green"),("Red","Orange"),("Yellow","Blue"),("Yellow","Red"),("Red","Red"),("Red","Yellow")]))

# the itertools.permutations creates a list of all possible combinations of the input tuples and stores them in a list 
# I know this is a terrrrribly inefficient method that uses "brute force" to load a dictionary of all possible combinations of paths, 
# as the permutations method itself is of O(n!) complexity. ie. 5 input tuples = 120 possibilities. 10 input tuples = 3,628,800 possibilities

print len(combos)
newlist = [] #array that stores combinations that pass checkFrontBack method
superlist = [] #array that stores combinations that have passed checkFrontBack and checkArrangement methods
goal = ("Blue","Green")
count = 0 


# this method takes in a list of all permutations of the given input tuples, checks to see that the front and back of each sub-list is matches
# the goal tuple, and then adds the permutations that satisfy this to newlist. 
def checkFrontBack(combos):
	for x in range(0,len(combos)):
		bucket = combos[x]
		front = bucket[0]
		back = bucket[len(bucket)-1]
		if front[0] == goal[0]:
			if back[1] == goal[1]:
				newlist.append(bucket)

# this method accepts a list of lists that have correct front and back tuples, and checks to see whether subsequent tuples have tuple[0] values that
# are equal to previous tuple[1] value. 
def checkArrangement(newlist):
	for n in range(0,len(newlist)):
		count = 0
		item = newlist[n]
		for i in range(1,len(item)):
			temp = item[i-1]
			temp1 = item[i]
			if temp[1] == temp1[0]:
				count+=1
				if count == len(item)-1:
					superlist.append(item)

# this method accepts superlist containing x valid combinations or no valid combinations.
def output(superlist):
	if len(superlist) == 0:
		print "Cannot unlock master panel!"
	else:
		if len(superlist) == 1:	
			print "There is",len(superlist),"possible combination that unlocks the master panel. It is:\n"
			for l in range(0,len(superlist)):
				print "\n"
				print superlist[l]
				print "\n"
		else: 
			print "There are",len(superlist),"possible combinations that unlocks the master panel. They are:\n"
			for l in range(0,len(superlist)):
				print "\n"
				print superlist[l]
				print "\n"

## test for checkFrontBack: this should only add the front list to newlist 
# testlist = [(("Blue","Green"),("Red","Green")),(("Yellow", "Red"),("Blue","Green")),(("Blue","Red"),("Orange","Red"))]
# checkFrontBack(testlist)
# print newlist

##test for checkArrangement: this should only add the front list to testlist2
# testlist2 = [(("Blue","Red"),("Red","Green")),(("Yellow", "Red"),("Blue","Green")),(("Blue","Red"),("Orange","Red"))]
# checkArrangement(testlist2)
# print superlist

checkFrontBack(combos)
checkArrangement(newlist)
output(superlist)




