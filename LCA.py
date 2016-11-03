from collections import defaultdict

data_dict = defaultdict(list)

string1="Frank->Mary,Mary->Sam,Mary->Bob,Sam->Kattie,Sam->Pete,Bob->John,Pete,John"
string2="Sam->Pete,Pete->Nancy,Sam->Kattie,Mary->Bob,Frank->Mary,Mary->Sam,Bob->John,Nancy,Kattie"
input=string2.split(',')

word = [elem.strip().split('->') for elem in input]
newWord=word[0:-2]
dic = defaultdict(list)

dictlist=[]

def intersect(a, b):
	return list(set(a) & set(b))

def search(dic, searchFor):
    for k in dic:
        for v in dic[k]:
            if searchFor in v:
                return k
    return None
			
for item in newWord:                                                                                                
	key = "/".join(item[:-1])    
	dic[key].append(item[-1])

a=word[-2]
strA=''.join(a)
b=word[-1]
strB=''.join(b)

liststr1=[]
liststr2=[]
liststr1.append(strA)
liststr2.append(strB)
x,y="",""
for i in range(len(dic)):
	x=search(dic,strA)
	if x is None:
		break
	liststr1.append(x)
	strA=x
		
for i in range(len(dic)):
	y=search(dic,strB)
	if y is None:
		break
	liststr2.append(y)
	strB=y
			
z=[]

for k in liststr1:
	if k in liststr2:
		print (k)
		break
		








