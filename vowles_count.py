'''
# Author: ryan
# Date: Oct. 7 20:30
# Note: count the num of vowles in a string.
'''

def vowles_count(str):
	ncount = 0
	for ch in str:
		if ch in 'aeiouAEIOU':
			ncount += 1
			
	return ncount
	
ncount = vowles_count("hello world")
print ("hello world contains ", ncount, "vowles." )
