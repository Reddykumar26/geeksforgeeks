list1=["gfg is 4","all no 1","geeks over 7 seas","and 100 planest"]
dict1={}
for x in list1:
	z=x.split(" ")
	for y in z:
		if y.isdigit():
			k=int(y) # k =4 if k not taken '1' is stored as string for key 
			dict1[k]=x 
print(dict1)
list5 = sorted(dict1) # list5 returns list
list6 = []
for x in list5:
	list6.append(dict1[x])
print(list6)



"""
list1=["gfg is 4","all no 1","geeks over 7 seas","and 100 planest"]
dict1={}
list2=[]
list3=[]
list4=[]
for x in list1:
	x=x.split(" ")
	for y in x:
		if y.isdigit():
			k=int(y)
			dict1[k]=x 
print(list1)
for x in dict1.keys():
	list2.append(x)

list2.sort()
for x in list2:
	list3.append(dict1[x])

for x in list3:
	k=' '.join(x)
	list4.append(k)
print(list4)

"""
