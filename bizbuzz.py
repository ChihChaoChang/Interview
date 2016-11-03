import sys

def Outthink(n,a,b):
		results = []
		IntN=int(n)
		IntA=int(a)
		IntB=int(b)
		for i in range(1, IntN+1):
			if (i % IntA == 0 and a in str(i)) :
				results.append("OUTTHINK")
			elif (i % IntB == 0 and b in str(i)):
				results.append("OUTTHINK")
			elif (i % IntA == 0 and a not in str(i)):
				results.append("OUT")
			elif (i % IntB == 0 and b not in str(i)):
				results.append("OUT")
			elif ( a in str(i) and i % IntA != 0):
				results.append("THINK")
			elif ( b in str(i) and i % IntB != 0):
				results.append("THINK")	
			else:
				results.append(str(i))
		return results
string=input("Please enter N, p, q\n")
input=string.split(',')


x=Outthink(input[0],input[1],input[2])

str1 = ','.join(x)
print (str1)
#print (x)
