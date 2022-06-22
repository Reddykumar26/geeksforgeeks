list1=[3,3,3,3,6,7,5,5,5,8,8,6,6,6,6,6,1,1,1,2,2]
#		output=[12,36,7,15,16,3,4]	
list2=[]
list3=[]
for x in list1:
	if x not in list2:
		list2.append(x)
print(list2)
for i in list2:
	list3.append(i*int(list1.count(i)))
print(list3)
