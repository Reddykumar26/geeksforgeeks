list1=[[1,2],[3,4],[4,5]]
list2=[[1,2],[1,6],[3,4]]
list3=[]
k=max(len(list1),len(list2))
for i in list1:
	if i  not in list2:
		list3.append(i)
for i in list2:
	if i  not in list1:
		list3.append(i)
print(list3)
