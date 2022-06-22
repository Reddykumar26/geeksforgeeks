list1=[12,34,56]
print(list1)
list2=[]

for x in list1:
	
	x=str(x)
	print(x)
	k=0
	for i in x:
		k=k+int(i)
	list2.append(k)
print(list2)

