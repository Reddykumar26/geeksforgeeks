list1=["Gfg is best for geeks","All love Gfg","Gfg is best for CS","For CS geeks Gfg is best"]
#list1=["Gfg is best for geeks","All love Gfg"]
list2=[]
list3=[]
dict1={}
for x in list1:
	k=[]
	print(x)
	list2=list2+x.split(" ")

print((list2))
for x in list2:
	if x not in list3:
		list3.append(x)
print(list3)
l=int(len(list2))
print(l)
for x in list3:

	dict1[x]=(float(list2.count(x)))/l
print(dict1)
