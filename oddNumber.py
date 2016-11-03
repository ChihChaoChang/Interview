def getOddOccurrence(arr):
	# Initialize result
	res = 0
    # Traverse the array
	for element in arr:
        # XOR with the result
		res = res^element
	return res
arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
x=getOddOccurrence(arr)
print (x)

