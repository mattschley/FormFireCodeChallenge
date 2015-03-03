# FormFireImprovement.py
# This script was written by Matt Schley as a part of the FormFire coding challenge. 
# 3/2/2014
# It is an improvement upon my old solution in a couple of ways: 
#
# 1) Instead of generating a list of all possible permutations of keys, this solution uses recursion to do a depth first search on the
#    list of chips that begin with chips that correspond to the goal state
# 2) This solution performs better on large input spaces, whereas the previous solution was limited by the permutations method
#    provided by itertools which was O(n!)
# 3) Simple begining checks insure that searches only occur on pairlists that contain at least one potential starting chip and ending chip that
#    corrsepond to the goal state's specifications


pairlist = [("Blue","Green"),("Red","Red"),("Green","Blue"),("Blue","Yellow"),("Blue","Green"),("Green","Yellow"),("Orange","Red"),("Red","Green"),("Red","Orange"),("Red","Orange"),("Yellow","Blue"),("Yellow","Red"),("Green","Yellow"),("Orange","Red"),("Red","Green"),("Yellow","Blue"),("Yellow","Red"),("Red","Red"),("Blue","Yellow"),("Blue","Green")]



#### THESE ARE THE THREE CASES THAT THE CODE CHALLENGE INCLUDED ####
#[("Blue","Green"),("Blue","Yellow"),("Red","Orange"),("Red","Green"),("Yellow","Red"),("Orange","Purple")]
#[("Blue","Green"),("Blue","Yellow"),("Red","Orange"),("Red","Green"),("Yellow","Red"),("Orange","Red")]
#[("Blue","Green"),("Blue","Green"),("Blue","Yellow"),("Green","Yellow"),("Orange","Red"),("Red","Green"),("Red","Orange"),("Yellow","Blue"),("Yellow","Red")]

# A FEW ADDITIONAL CASES
#[("Blue","Green"),("Blue","Yellow"),("Yellow","Red")]
#[("Blue","Green"),("Blue","Yellow"),("Yellow","Red"),("Red","Green")]
#[("Blue","Green"),("Blue","Yellow"),("Red","Red"),("Blue","Green"),("Green","Blue"),("Blue","Yellow"),("Blue","Green"),("Green","Yellow"),("Orange","Red"),("Red","Green"),("Red","Orange"),("Red","Orange"),("Yellow","Blue"),("Red","Green"),("Yellow","Blue"),("Yellow","Red"),("Red","Red"),("Yellow","Red"),("Green","Yellow"),("Orange","Red")]
#[("Blue","Green"),("Red","Red"),("Green","Blue"),("Blue","Yellow"),("Blue","Green"),("Green","Yellow"),("Orange","Red"),("Red","Green"),("Red","Orange"),("Red","Orange"),("Yellow","Blue"),("Yellow","Red"),("Green","Yellow"),("Orange","Red"),("Red","Green"),("Yellow","Blue"),("Yellow","Red"),("Red","Red"),("Blue","Yellow"),("Blue","Green")]

goal = []
stack = []
final = []
count = 0

# accept pairlist as input, pull goal from pairlist, call getFirst on goal state and pairlist
def getGoal(pairlist):
	global goal
	goal = pairlist[0]
	pairlist.remove(goal)
	getFirst(goal,pairlist)

# accepts goal state and pairlist from above
# make sure potential starting chip and ending chip exist in pairlist - if they don't, then cannot unlock master lock
# if they do exist, run next on first possible chip
# if multiple potential starting chips exist, and first potential chip chosen doesn't lead to solution, 
# this function will be called recursively from below
def getFirst(goal,list1):
	possiblestart = []
	possibleend = []
	global stack
	for pairs in list1:
		if pairs[0] == goal[0]:
			possiblestart.append(pairs)
		if pairs[1] == goal[1]:
			possibleend.append(pairs)

	if (len(possiblestart)==0): # if no possible starting chip exists, cannot unlock
		print "Cannot unlock master lock"

	if (len(possibleend)==0): # if no possible ending chip exists, cannot unlock
		print "Cannot unlock master lock"
		
	if (len(possiblestart)>=1) and len(possibleend)!=0:
		final.append(possiblestart[0])
		pairlist.remove(possiblestart[0])
		return next(possiblestart[0],pairlist) 

# takes in a current chip and the list of available pairs as input 
# if possible next move exists, call next on it and add it to the final list of chips
# if no possible next move exists and all chips haven't been used, pop from final stack list 
# do this until recusive depth of 100 is reached or until no possible chips exist due to all of
# them being used in a correct solution that unlocks the lock
def next(possiblestart, pairlist):
	ans = []
	possible = []
	for pairs in pairlist:
		if pairs[0] == possiblestart[1]:
	 		possible.append(pairs)

	# if the current chip has possible next chips, pick one and find its next chips
	if len(possible)!= 0: 
		for i in possible:
			temp = i
			final.append(i) # add chip to final list
			pairlist.remove(i) # remove from pairlsit 
			return next(temp,pairlist) # find chip's next chip

	# if the current chip has no possible next chips
	if len(possible)==0: 
		# if the current chip has no possible next chips and has possible pairs left
		if len(pairlist)!=0: 
			global count
			# if the final list is empty, call GetFirst to ensure we start with correct chips
			if len(final)==0: 
				getFirst(goal,pairlist) 

			# if we have two or more in final, pop two elements - need this to insure we don't pop from empty list
			if len(final) >= 2: 
				temp = final.pop()
				temp1 = final.pop()
				pairlist.append(temp) 
				pairlist.append(temp1) 
			count = count + 1
			length = len(final)

			# this prevents infintite loops and breaking pythons maximum recursion depth 
			if count < 100: 
				for y in pairlist:
					# find chip that matches last chip in final
					if y[0] == final[length-1][1]: 
						pairlist.remove(y) 
						final.append(y) 
						return next(y,pairlist) 

			# break out of program if deep search fails to return soultion after 100 calls
			else: 
				print '\n'
				print "Cannot unlike master panel"
				exit()

		# if we've used all of the pairs, and last element matches goal state, we have a correct solution! print it!
		elif len(pairlist)==0: 
			leng = len(final)
			temp = final[leng-1]
			if temp[1] == goal[1]:
				print '\n'
				print '==================='
				print '\n'
				print "FINAL =",final

getGoal(pairlist)



