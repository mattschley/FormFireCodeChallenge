FormFireCodeChallenge
=====================

The input for this script consists of a goal tuple ("Color","Color") indicating the beginning and ending marker colors for our master lock, followed by a series of chip definitions stored as tuples. The goal is to arrange the colored chips in a way that allows them to go from the starting color in the goal state to the ending color in the goal state, unlocking our lock.   

My code uses the Python itertools library and the permutations method to accept an arrangement of chip tuples. I define the goal tuple as being ("Blue","Green") which is the goal for each of the three supplied examples. I define the collection of chip tuples inside the combos = list(itertools.permutations([collection of chips])) declaration. 

Combos is a dictionary-like list containing every possible permutation of the input chips. I call a method checkFrontBack on this list in order to reduce it to only those lists that have the first element in the first tuple in their arrangement equal to "Blue" and the last element in the last tuple of their list equal to "Green". I then call a method checkArrangement on this shortened list of permutations to reduce the list even further to contain only those solutions that contain valid arrangements (ie. ("Orange","Red") next to ("Red","Green")). The resulting list contains only those arrangements of chips that 1) start and end according to the goal chip and 2) only contain valid collections of chips. This list is the exact list of combinations that unlock the master lock. 

If I were to do this challenge again with more time, I would use a more efficient search technique to handle larger sets of chips. The permutations method that I used is O(n!), making this dictionary-based solution extremely inefficient for collections of chips only slightly larger than the length supplied by the example inputs. Although the program runs in about a second for chip collections of size 9, it begins to lose practicality after that. 

My ideal solution would start by finding the possible front chips, and navigating down their paths. If I reached a point where a given chip was unable to match another or I had used every chip and reached a state that didn't match the goal, I would backtrack to a point that was valid, even if that meant returning to the begining chip choice. By backtracking and using a good hueristic instead of brute forcing every combination, I could create a much more efficient algorithm for searching larger collections of chips. 
