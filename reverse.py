
my_string1="Hello Watrson"
my_string2="Thou art thyself though not a Montague - from Romeo and Juliet"
NewString=my_string2[::-1]
for i, c in enumerate(NewString):
	if not c.isdigit():
		break
x=NewString[:i] + NewString[i:].capitalize()
y=NewString.title()

print (x)
print (y)
