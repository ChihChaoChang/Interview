import sys

def reversed(x):
	return int(bin(x)[:1:-1], 2)# reverse the 01 and remove prefix 'ob'
	
if __name__ == "__main__":
	num = raw_input()	
	try:
		number=int(num)
		if (number >= 1 and number <= 1000000000):
			print reversed(number)
		else:
			raise
	except Exception:
		print "Enter again"




