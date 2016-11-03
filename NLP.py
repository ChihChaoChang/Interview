string1="(NP (NP (DT a) (MN boy)) (VP (VBG eating) (NP (NMS sausages))))"
string2="(NMS sausages)"
string3="(NP (DT a) (MM boy))"
x=string3.split()

list=[]
for k in range(len(x)):
	if ")" in x[k]:
		list.append(x[k])
for result in list:
        result = ' '.join(list)
result= ''.join(c for c in result if c not in '(){}<>')

print (result)
