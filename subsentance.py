import re
from collections import defaultdict
string="IBM cognitive computing|IBM ""cognitive"" computing is a revolution| ibm cognitive   computing |'IBM Cognitive Computing' is a revolution?"

removelist = "| "
stringNew=" ".join(string.split())
mystring=stringNew.lower().strip()

mylist=re.sub(r'[^\w'+removelist+']', '',mystring)
#print (mylist)
for x in mylist.split("|"):
	x.lstrip().rstrip()
splitmylist=mylist.split("|")


line=string.split("|")

#print (splitmylist)

subsentance_dict = {}
for i in range(len(line)):
    subsentance_dict[line[i]] = splitmylist[i]
#print (subsentance_dict)

for i in range(0,len(splitmylist)-1):
	splitmylist[i]=splitmylist[i].lstrip().rstrip()
	
for x in subsentance_dict:
	subsentance_dict[x]=subsentance_dict[x].lstrip().rstrip()
	#print(subsentance_dict[x])
#print(splitmylist)

for y in splitmylist:
	for x in subsentance_dict.keys():
		if subsentance_dict[x] in y and subsentance_dict[x]!= y:
			subsentance_dict[x]="N"
		else:
			pass
#print (subsentance_dict)
#key=(sorted(subsentance_dict.values(), key=len)[-1])
#key=str(key)

for x in subsentance_dict.keys():
	if subsentance_dict[x] != "N":
		print (x)
	

#print (subsentance_dict)
