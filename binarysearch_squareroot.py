'''
Author: ryan
Date: Oct. 7 09:05
Note: use the method called binary search to calculate the square root of an positive num.
'''

def test():
	pass
	
def sqrt_fun(x):
	high = x
	low = 0
	guess = (low + high) / 2

	while abs(guess ** 2 -x)> 1e-4 :
		if guess ** 2 > x:
			high = guess
		else:
			low = guess
		
		guess = (low + high) / 2	
		
	print ('the square root of x is: ',guess)
		
while True:	
	str = input("please input a positive integer: ")
	try:
		x = float(str)
	except ValueError:
		if str == 'q':
			ans = input("do you want to quit?[y/n]")
			if ans == 'y':
				break
			else:
				continue
		else:
			print ("input error!")
			continue

	if x == 0:
		print ('the root of x is: ', 0)
		continue
	elif x < 0:
		print ("this integer is negtive, error!")
	else:	
		sqrt_fun(x)

