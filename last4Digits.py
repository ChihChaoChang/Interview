import re
mystr = "abcdefghijkl"
x=mystr[-4:]
y=mystr[:-4]


#print(x)
#print(y)

length=len(y)
newY="#"*length

#print (newY)

combine=newY+x
print (combine)
